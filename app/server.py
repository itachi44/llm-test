from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from langserve import add_routes
from langchain.chains import LLMChain
from langchain_openai import OpenAI, ChatOpenAI
import chainlit as cl
from .configs import *
import os


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

ROUTER_LLM = GoogleGenerativeAI(
    model="gemini-1.5-pro",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

SQL_LLM = GoogleGenerativeAI(
    model="gemini-1.5-pro",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

LLM_RESUMER = GoogleGenerativeAI(
    model="gemini-1.5-pro",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

LLM_MISSING_DATA = GoogleGenerativeAI(
    model="gemini-1.5-pro",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

LLM_SQL_CORRECTOR = GoogleGenerativeAI(
    model="gemini-1.5-pro",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


def determine_database(query: str) -> str:
    """
    Utilise le LLM pour déterminer la base de données cible.
    """
    inputs = {
        "mesx_metadata": MESX_METADATA,
        "prod_metadata": PROD_METADATA,
        "query": query
    }

    response = ROUTER_LLM.invoke(ROUTER_PROMPT.format(**inputs))
    return response.strip()


def clean_response(response: str) -> str:
    """
    Nettoie les sauts de ligne et espaces inutiles dans une réponse.
    """
    return response.replace("\n", " ").strip()


async def generate_sql(query: str, target_db: str, client_id: str, site_id: str) -> str:
    """
    Génère une requête SQL en fonction de la base de données cible et des paramètres client_id et site_id.
    """
    if target_db == "mesx":
        schema = mesx_schema
        examples = mesx_examples
    else:
        schema = prod_schema
        examples = prod_examples
    
    inputs = {
        "schema": schema,
        "examples": examples,
        "query": query,
        "client_id": client_id,
        "site_id": site_id,
    }

    formatted_prompt = SQL_GENERATION_PROMPT.format(**inputs)
    result = await SQL_LLM_invoke_async(formatted_prompt)
    return result

SQL_LLM_invoke_async = cl.make_async(SQL_LLM.invoke)

async def handle_query(query: str, client_id: str, site_id: str):
    """
    Gère une requête utilisateur :
    1. Détermine la base de données cible.
    2. Génère une requête SQL.
    3. Exécute et retourne le résultat.
    """
    try:
        target_db = determine_database(query)          

        sql_query = await generate_sql(query, target_db, client_id, site_id)

        # print("SQL Query:", sql_query)

        corrected_query = await correct_sql_syntax(sql_query, target_db)

        corrected_query = corrected_query.replace("`", "").replace("sql", "")

        if target_db == "mesx":
            execute_query_tool = mesx_query_tool
        else:
            execute_query_tool = prod_query_tool

        result = await cl.make_async(execute_query_tool.invoke)({"query": corrected_query})

        # print("Query result:", result)
        return result

    except Exception as e:
        print(f"Erreur dans handle_query pour la requête '{query}': {str(e)}")
        return "donnée manquante"



async def get_summary_data(client_id: str, site_id: str) -> dict:
    """
    Pose 6 questions au LLM pour récupérer les données de la veille,
    exécute les requêtes SQL correspondantes, et retourne un dictionnaire formaté.
    """
    summary_data = {}

    questions = [
        ("Récupère les consignes de la veille", "consignes"),
        ("Récupère les indicateurs de performance de la veille (TRS, performance, qualité, disponibilité).", "performance_indicators"),
        ("Récupère le temps d'avance ou de retard en heures sur les ordres de fabrications (OF) de la veille : si ça dépasse 24h on a un retard.", "of_info"),
        ("Récupère le nombre de produits fabriqués la veille grace aux données des capteurs", "product_count"),
        ("Compte le nombre de rebuts générés la veille.", "scrap_count"),
        ("Récupère le nombre d'arrêts machines de la veille.", "stoppages")
    ]

    for query, key in questions:
        # print(f"Current query : {query}")
        summary_data[key] = await handle_query(query, client_id, site_id)
    
    return summary_data


async def generate_summary(summary_data: dict) -> str:
    """
    Génère un résumé structuré et concis basé sur les données du quart.
    Utilise le LLM LLM_RESUMER pour générer le texte.
    """
    formatted_data = "\n".join([f"{key}: {value}" for key, value in summary_data.items()])
    prompt = summary_prompt.format(data=formatted_data)
    summary = await cl.make_async(LLM_RESUMER.invoke)(prompt)

    return summary.strip()


async def handle_missing_data(user_input: str, missing_keys: list):
    """
    Handles the extraction of missing data from user input.
    """

    inputs = {
        "missing_keys": missing_keys,
        "user_input": user_input
    }

    missing_data_full_prompt = missing_data_prompt.format(**inputs)
    result_data = await cl.make_async(LLM_MISSING_DATA.invoke)(missing_data_full_prompt)
    
    return result_data.strip()


async def correct_sql_syntax(raw_query: str, target_db: str) -> str:
    """
    Corrige la syntaxe d'une requête SQL en fonction du schéma de la base de données cible.
    """
    schemas = mesx_schema if target_db == "mesx" else prod_schema
    inputs = {
        "schemas": schemas,
        "query": raw_query
    }
    formatted_prompt = sql_syntax_fix_prompt.format(**inputs)
    
    try:
        corrected_query = await cl.make_async(LLM_SQL_CORRECTOR.invoke)(formatted_prompt)
        return clean_response(corrected_query)
    except Exception as e:
        print(f"Erreur dans correct_sql_syntax pour la requête '{raw_query}': {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erreur lors de la correction SQL: {str(e)}")



@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


@app.get("/summary")
async def get_summary(client_id: str, site_id: str):
    """
    Route pour générer un résumé structuré des données collectées.
    """
    try:
        summary_data = await get_summary_data(client_id, site_id)
        summary_text = await generate_summary(summary_data)
        return {"summary": summary_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/query")
async def handle_user_query(query: str, client_id: str, site_id: str):
    """
    Route pour gérer les requêtes utilisateur.
    """
    try:
        result = handle_query(query, client_id, site_id)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/sql_query")
async def generate_sql_for_query(query: str, client_id: str, site_id: str):
    """
    Route pour générer des requêtes SQL basées sur une question utilisateur.
    """
    try:
        target_db = determine_database(query)
        sql_query = await generate_sql(query, target_db, client_id, site_id)
        clean_sql_query = clean_response(sql_query)
        return {"sql_query": clean_sql_query}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/correct-sql")
async def correct_sql(query: str, target_db: str):
    """
    Route pour corriger une requête SQL en fonction du schéma de la base de données cible.
    """
    try:
        corrected_query = await correct_sql_syntax(query, target_db)
        return {"corrected_query": corrected_query}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



add_routes(app, ROUTER_LLM, path="/llm")
add_routes(app, SQL_LLM, path="/SQL_LLM")
add_routes(app, LLM_RESUMER, path="/summary_generator")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)