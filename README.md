Ce dossier, P7, est le projet 7 avant que je ne fasse le docker init. J'ai cloné le projet qui s'appelle maintenant Projet_7 dans lequel je fais le docker init.


Build l'image Docker:

docker build \
-t predictionsentiments \
-f Projet_7_API/Dockerfile Projet_7_API

Runner l'image Docker:
docker run -p 8000:8000 --name predictionsentiments_container predictionsentiments

POur accéder à la documentation:
http://0.0.0.0:8000/docs

Pour vérifier où mes images docker sont:
container registries dans la barre de recherche Azure
predictionsentimentsregistry est mon registry situé dans mes Dépôts Azure