
from sqlalchemy import create_engine, inspect

def extract_metadata(pg_uri):
    """Retourne le schéma de la base de données sous forme textuelle."""
    engine = create_engine(pg_uri) 
    inspector = inspect(engine) 

    metadata = "\n".join(
        [
            f"Table: {table}\n" + "\n".join(
                [f"  - {col['name']} ({col['type']})" for col in inspector.get_columns(table)]
            )
            for table in inspector.get_table_names()
        ]
    )
    return metadata


def format_schema(schema_text):
    """Nettoie et formate le schéma extrait pour une utilisation dans des prompts."""
    tables = schema_text.split("Table: ")
    formatted_schema = "Base de données contenant les tables suivantes :\n"
    for table in tables[1:]:
        lines = table.split("\n")
        table_name = lines[0].strip()
        columns = "\n".join(
            f"  - {line.strip().replace('- ', '')}" 
            for line in lines[1:] 
            if line.strip() and "- " in line
        )
        formatted_schema += f"Table {table_name} :\n{columns}\n\n"
    return formatted_schema


def format_examples(query_examples):
    """
    Formate les exemples de requêtes pour les inclure dans le prompt.
    """
    examples_text = ""
    for example in query_examples:
        examples_text += f"- Question : {example['question']}\n  Requête : {example['sql']}\n"
    return examples_text