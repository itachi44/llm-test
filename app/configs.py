import os
from langchain_openai import ChatOpenAI, OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import TransformChain
from langchain.chains import LLMChain
from langchain_community.embeddings import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity # type: ignore
from langchain.chains.router import RouterChain
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from fastapi.middleware.cors import CORSMiddleware
from .utils import extract_metadata, format_schema, format_examples
from .metadata import db_metadata, table_descriptions, query_examples, PRODUCTION_SOURCE
from dotenv import load_dotenv
from urllib.parse import quote_plus


load_dotenv()

username = os.getenv("ISOPROD_USERNAME")
password = quote_plus(os.getenv("ISOPROD_PASSWORD"))
host = os.getenv("ISOPROD_HOST")
port = os.getenv("ISOPROD_PORT")

prod_db = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/prod"
mesx_db = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/mesx"

db_1 = SQLDatabase.from_uri(prod_db)
db_2 = SQLDatabase.from_uri(mesx_db)

mesx_query_tool = QuerySQLDataBaseTool(db=db_2)
prod_query_tool = QuerySQLDataBaseTool(db=db_1)


mesx_schema_raw = extract_metadata(mesx_db)
prod_schema_raw = extract_metadata(prod_db)

mesx_schema = format_schema(mesx_schema_raw)
prod_schema = format_schema(prod_schema_raw)

mesx_examples = format_examples(query_examples["mesx"])
prod_examples = format_examples(query_examples["prod"])

MESX_METADATA = f"{db_metadata['mesx']}\n\n{mesx_schema}\n\nDescriptions des tables :\n"
for table, description in table_descriptions["mesx"].items():
    MESX_METADATA  += f"- {table}: {description}\n"

PROD_METADATA = f"{db_metadata['prod']}\n\n{prod_schema}\n\nDescriptions des tables :\n"
for table, description in table_descriptions["prod"].items():
    PROD_METADATA += f"- {table}: {description}\n"


ROUTER_TEMPLATE = """
Voici des informations sur deux bases de données :

1. Base de données 'mesx' : {mesx_metadata}
2. Base de données 'prod' : {prod_metadata}

Question : {query}

Sur quelle base de données pensez-vous que cette question doit être exécutée ? Répondez uniquement par 'mesx' ou 'prod'.
"""
ROUTER_PROMPT = PromptTemplate(
    input_variables=["mesx_metadata", "prod_metadata", "query"],
    template=ROUTER_TEMPLATE
)


SQL_SYNTAX_FIX_PROMPT_TEMPLATE = """
Vous êtes un assistant expert en bases de données et SQL. Votre tâche est de corriger la syntaxe des requêtes SQL fournies pour qu'elles soient valides et exécutables. Vous disposez également des schémas des tables pour vérifier et ajuster la syntaxe. Suivez les consignes ci-dessous :

- Supprimez tout texte qui n'est pas une commande SQL valide.
- Enlevez tous les guillemets inversés (backticks) et mot clefs si nécessaire comme par exemple (```sql).
- Vérifiez et corrigez la syntaxe SQL (par exemple, orthographe des mots-clés, placement des virgules, ou utilisation des clauses).
- Conservez uniquement les instructions SQL et excluez tout commentaire ou texte non exécutable.
- Les colonnes dans les instructions doivent exister réellement et être en adéquation avec les schemas utilisés.
- Si une instruction semble incomplète ou non valide, reformulez-la pour qu'elle devienne valide.
- Gardez un style SQL lisible et cohérent.
- Si la requête est syntaxiquement correcte, ne la modifiez pas.

Voici les schémas des tables disponibles :
{schemas}

Voici la requête brute :
{query}

Analyse et corrige si nécessaire cette requête.
Ne retourne que la requête corrigée et rien d'autre.
Pas d'explication ou de commentaire, juste la requête SQL corrigée.
"""

sql_syntax_fix_prompt = PromptTemplate(
    input_variables=["schemas", "query"],
    template=SQL_SYNTAX_FIX_PROMPT_TEMPLATE
)


SQL_GENERATION_TEMPLATE = """
Vous êtes un expert SQL. Voici des informations sur la base de données sélectionnée :

Schéma :
{schema}

Exemples de requêtes :
{examples}

Écrivez une requête SQL pour répondre à la question suivante. 
Fournissez uniquement une requête SQL valide et met jamais de commentaire, d'explication de backticks ou de guillemets.
- Si on ne précise rien, il faut toujours récupérer les données des dernières 24 heures.
- N'utilisez jamais la fonction 'date' car elle ne fonctionne pas, utilisez plutôt 'current_date' ou 'now()'.
- Il faut toujours caster les dates en timestamp pour les comparaisons, même si la colonne est de type date.
- Quand on vous donne le client et le site, il faut toujours les utiliser dans la requête en ajoutant une condition :
  WHERE client_id = '{client_id}' AND site_id = '{site_id}'
- Il faut toujours veiller à ce que la requête soit basée sur le schéma fourni et les bonnes colonnes des tables.

Ne fournissez aucune explication supplémentaire, balise Markdown ou mot clé autre que la requête SQL :
Question : {query}
"""
SQL_GENERATION_PROMPT = PromptTemplate(
    input_variables=["schema", "examples", "query", "client_id", "site_id"],
    template=SQL_GENERATION_TEMPLATE
)


SUMMARY_PROMPT_TEMPLATE = """
Vous êtes un assistant expert en gestion industrielle. Votre tâche est de générer un résumé structuré et concis basé sur les données suivantes. Soyez clair, professionnel, et direct. Voici les données :

{data}

Générez un résumé intitulé "Résumé de quart" en titre. Le résumé doit inclure :
- Une introduction très brève (une phrase).
- Les consignes principales si disponibles si c'est vide met donnée indisponible puis on te les fournira.
- Les indicateurs clés de performance (TRS, performance, qualité, disponibilité).
- Le nombre de produits fabriqués, le nombre de rebuts, et les arrêts machines.
- Les informations sur le retard ou l'avance sur les Ordres de Fabrication :
Il faut fournir seulement le nom de l'of et son temps de retard ou d'avance en heure (NOW - date mise à jour), pas besoin d'ajouter un where sur le start_date.
Il s'agira que des ordres de fabrication en cours (WHERE status=2), n'ajoute pas de détails textuels.

Tous les indicateurs sont des pourcentages.
Si une données est manquante ou vide ou nulle met juste donnée indisponible et après on te les fournira.
Ne crée rien, fait juste le résumé de ce que tu voies.

Restez professionnel, limitez le texte explicatif et soyez précis. Le ton doit être neutre et formel.
Formatte le texte avec des bullet points pour chaque rubrique.
Ce résumé doit aider l'opérateur qui reprend le quart à connaitre toutes les informations nécessaires de la veille.
"""

summary_prompt = PromptTemplate(
    input_variables=["data"],
    template=SUMMARY_PROMPT_TEMPLATE
)


ROUTER_EXTRACTION_TEMPLATE = """
Voici une liste de clés manquantes : {missing_keys}

Et voici le texte brut saisi par l'utilisateur :
---
{user_input}
---

Votre tâche est d'extraire intelligemment la donnée manquante et de l'organiser en `clé=valeur` qui correspondent aux clés manquantes. 
Assurez-vous que le format soit strictement un dictionnaire.

Si une clé manquante n'est pas présente dans le texte, ignorez-la.

Exemple :
- Clés manquantes : [performance, qualité]
- Texte utilisateur : 'performance est de 85 qualité est 90 d'autres informations inutiles'

N'ajoute pas de texte supplémentaire, ne fais pas de calculs, et ne retourne que le dictionnaire sans commentaire ou explication.

Ne met pas de mot clé du genre dict ou json etc, pas de balise Markdown ou de commentaire.
Fait aussi attention aux quotes que tu mets dans les valeurs du dictionnaire.
"""

missing_data_prompt = PromptTemplate(
    input_variables=["missing_keys", "user_input"],
    template=ROUTER_EXTRACTION_TEMPLATE
)