# Juno Assistant

Juno Assistant est une application Chainlit permettant de construire une interface utilisateur pour interagir avec des fonctions basées sur des modèles de langage.

---

## Installation

Pour utiliser Juno Assistant, suivez les étapes ci-dessous :

### Prérequis

1. Installez Python 3.12 (ou une version compatible).
2. Installez `pip` et `poetry` si ce n'est pas déjà fait :

   ```bash
   pip install poetry


### Lancer l'application avec Docker :

Ce projet inclut un Dockerfile.chainlit permettant de construire et d’héberger facilement votre application Chainlit.

#### Construire l’image Docker

Pour construire l’image, exécutez :

```bash
docker build -f Dockerfile.chainlit -t juno-wrapup .
```

Pour démarrer le conteneur, exécutez : 

```bash
docker run -d -p 8000:8000 --name juno-chainlit juno-wrapup
```

Une fois le conteneur lancé, ouvrez un navigateur et accédez à :

```
http://localhost:8000
```