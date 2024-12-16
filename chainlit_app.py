from typing import cast
import chainlit as cl
import re
import json
from app.server import handle_query, generate_summary, get_summary_data, handle_missing_data


async def configure_client(user_input: str):
    clients = {
        "agriplas": ("6HEKREQoh5VTRUVmoU1N", "kCtdls2erLuoMormNjwY"),
        "nutriset": ("BcI33o5TwfTtfecpno2x", "0P8s5fIbIjuQKCJKIPe3"),
        "lennox": ("kAn5DltVwDo3XTJ7LmKT", "2xOCawpSjhgzqWXpMXNZ")
    }

    for client_name, (client_id, site_id) in clients.items():
        if client_name in user_input.lower():
            cl.user_session.set("client_id", client_id)
            cl.user_session.set("site_id", site_id)
            return f"Configuration terminée : client_id={client_id}, site_id={site_id}. Vous pouvez maintenant poser vos questions ou demander un résumé."

    return "Client inconnu. Veuillez vérifier le nom et réessayer."


@cl.on_chat_start
async def on_chat_start():
    """
    Initialisation de la session de chat.
    """
    cl.user_session.set("mode", "interactive")
    cl.user_session.set("missing_keys", None)
    cl.user_session.set("summary_data", None)
    
    await cl.Message(
        content="Bienvenue ! Veuillez fournir le nom du client pour lequel vous souhaitez un rapport."
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    """
    Gestion des messages utilisateur.
    """
    user_input = message.content.strip()
    
    missing_keys = cl.user_session.get("missing_keys")
    if missing_keys:
        try:
            user_data = await handle_missing_data(user_input, missing_keys)
            try:
                user_data = json.loads(user_data)
            except json.JSONDecodeError:
                user_data = {key: "donnée manquante" for key in missing_keys}

            if not user_data:
                raise ValueError("Aucune donnée valide trouvée pour les clés manquantes.")

            summary_data = cl.user_session.get("summary_data")
            summary_data.update(**user_data)

            cl.user_session.set("missing_keys", None)
            cl.user_session.set("summary_data", summary_data)

            summary = await generate_summary(summary_data)
            await cl.Message(content=summary).send()
        except Exception as e:
            await cl.Message(content=f"Erreur dans la mise à jour des données manquantes : {str(e)}.").send()
        return

    if user_input and not cl.user_session.get("client_id") and not cl.user_session.get("site_id"):
        try:
            response = await configure_client(user_input)
            await cl.Message(content=response).send()

        except Exception as e:
            await cl.Message(content=f"Erreur dans la configuration : {str(e)}. Veuillez vérifier que le nom du client se trouve dans les données.").send()
        return

    client_id = cl.user_session.get("client_id")
    site_id = cl.user_session.get("site_id")

    if not client_id or not site_id:
        await cl.Message(
            content="Veuillez d'abord fournir votre `client_id` et `site_id` au format : `client_id=XXX site_id=YYY`."
        ).send()
        return

    if "résumé" in user_input.lower() or "resume" in user_input.lower():
        await cl.Message(content="Génération du résumé en cours, patientez un peu...").send()

        try:
            summary_data = await get_summary_data(client_id, site_id)
            missing_data = {key: val for key, val in summary_data.items() if val == "donnée manquante" or val == '' }
            if missing_data:
                missing_keys = list(missing_data.keys())
                missing_keys = [key for key in missing_keys if key != "performance_indicators"]
                highlighted_keys = ", ".join([f"`{key}`" for key in missing_keys])
                cl.user_session.set("missing_keys", missing_keys)
                cl.user_session.set("summary_data", summary_data)

                await cl.Message(
                    content=f"Certaines données sont manquantes : {highlighted_keys}. Veuillez fournir ces données au format : `clé=valeur`. Vous pouvez inclure d'autres textes ou lignes, seules les informations nécessaires seront extraites."
                ).send()
                return

            summary = await generate_summary(summary_data)
            await cl.Message(content=summary).send()
        except Exception as e:
            await cl.Message(content=f"Erreur lors de la génération du résumé : {str(e)}").send()
    else:        
        await cl.Message(content="Traitement de votre requête...").send()

        try:
            response = await handle_query(user_input, client_id, site_id)
            response = re.sub(r"[^a-zA-Z0-9]+", ' ', response)
            await cl.Message(content=f"{response}").send()
        except Exception as e:
            await cl.Message(content=f"Erreur lors du traitement de la requête : {str(e)}").send()
