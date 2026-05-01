Ce dossier, P7, est le projet 7 avant que je ne fasse le docker init. J'ai cloné le projet qui s'appelle maintenant Projet_7 dans lequel je fais le docker init.


Build l'image Docker:

docker build \
-t predictionsentiments \
-f Projet_7_API/Dockerfile Projet_7_API

Runner l'image Docker:
docker run -p 8000:8000 --name predictionsentiments_container predictionsentiments

POur accéder à la documentation:
http://0.0.0.0:8000/docs

# AZURE PORTAL : Pour vérifier où mes images docker sont:
container registries dans la barre de recherche Azure
Services < dépôts 
predictionsentimentsregistry est mon registry situé dans mes Dépôts Azure
L'application est déployée via le 'app service'

# MLflow
Pour lancer MLFlow il faut taper 'mlflow server'
Ensuite, aller à http://127.0.0.1:5000/


# Lancer l'application
cd Projet_8_API
uvicorn main:app --host 0.0.0.0 --port 8000
uvicorn main:app --host 0.0.0.0 --port 8000 --reload



# Feeling classifier

Pour lancer l'API

fastapi dev main.py

Ouvir http://127.0.0.1:8000/docs

A faire:

- Installer Docker Desktop
- Faire un Dockerfile avec l'api dedans et qui marche
- Creer un Github
- Creer un Github workflow pour build l'image 
- Creer un compte Azure, creer une azure app 
- Deployer l'image de Github sur Azure app, 
- Avoir l'API qui fonctionne sur Azure APP