# Détecter les Bad Buzz grâce au Deep Learning et MLOps : Notre Démarche chez MIC

*Par [Votre Nom/Prénom]*

Dans un monde où l'image de marque se joue à la seconde sur les réseaux sociaux, pouvoir anticiper un "bad buzz" est crucial. C'est là que l'intelligence artificielle entre en jeu. Notre équipe chez **Marketing Intelligence Consulting (MIC)** a récemment développé pour la compagnie aérienne **Air Paradis** un système prédictif capable d'analyser le sentiment des tweets en temps réel. 

Ce projet visait non seulement à construire des modèles de pointe en compréhension du langage naturel (NLP), mais aussi à implémenter une architecture **MLOps** robuste pour déployer, suivre et améliorer ce modèle en production. Voici un retour d'expérience complet sur notre démarche.

---

## 1. Modélisation : Trois Approches pour un Même Objectif

Pour garantir les meilleurs résultats tout en maîtrisant la complexité, nous avons adopté une démarche itérative à travers trois niveaux de modélisation sur le dataset de référence *Sentiment140*.

### Approche 1 : Modèle sur Mesure Simple
Avant de nous plonger dans les architectures complexes, il est essentiel de définir une *baseline* (modèle de référence).
- **Technique** : Nous avons utilisé un modèle d'apprentissage classique (type Régression Logistique ou Naive Bayes) couplé à une représentation TF-IDF.
- **Avantages** : Très rapide à entraîner, peu gourmand en ressources et facilement interprétable.
- **Limites** : Ce modèle ignore le contexte séquentiel et sémantique plus fin des mots. Il a servi d'excellent point de comparaison, mais ses performances "plafonnent" sur du texte complexe comme les tweets.

### Approche 2 : Modèle sur Mesure Avancé (Deep Learning)
Pour capturer la sémantique complexe et le vocabulaire informel de Twitter, nous sommes passés aux réseaux de neurones.
- **Architecture** : Utilisation de TensorFlow/Keras avec une couche **Embedding** suivie de couches de *GlobalAveragePooling* et/ou réseaux récurrents.
- **Plongements lexicaux (Embeddings)** : Nous avons testé différentes représentations denses des mots pour capturer leur "sens". La représentation sous forme de séquences padées (jusqu'à 50 tokens) permet au modèle de traiter des vecteurs de taille fixe.
- **Résultats** : Une amélioration significative par rapport à la baseline, avec la capacité d'apprendre des relations entre les mots. *C'est ce modèle, offrant le meilleur compromis taille/performance, qui a été sélectionné pour la mise en production via notre API.*

### Approche 3 : Modèle Avancé avec BERT
La révolution du NLP se trouve dans les "Transformers".
- **Technique** : Nous avons expérimenté un modèle pré-entraîné **BERT** (Bidirectional Encoder Representations from Transformers). 
- **Avantages** : BERT prend en compte le contexte bidirectionnel de chaque mot (gauche et droite). Ses performances en classification de textes sont l'état de l'art.
- **Limites** : Ce modèle est extrêmement lourd et coûteux en inférence. Pour une contrainte financière nécessitant un hébergement Cloud gratuit pour notre MVP (App Service F1 sur Azure), déployer un modèle BERT brut posait des soucis de mémoire (RAM de 1 Go insuffisante). Cela a confirmé notre choix de déployer notre **Modèle sur Mesure Avancé (Approche 2)** en production.

---

## 2. Démarche MLOps : Du Notebook à la Production

Le développement du modèle n'est que la pointe de l'iceberg. L'essentiel du travail de l'AI Engineer réside dans la mise en production logicielle. L'approche MLOps (Machine Learning Operations) garantit la reproductibilité, le test et le suivi du modèle une fois déployé.

### A. Tracking et Gestion des Modèles avec MLFlow
Au lieu de sauvegarder manuellement nos essais avec des noms de fichiers chaotiques, nous avons intégré **MLFlow** (comme on le voit dans notre test [test_ml_flow.py](file:///Users/j/Documents/OC_Inge_IA/Projet_7/Projet_7_CX/test_ml_flow.py)).
- **Suivi des Expérimentations (Tracking)** : Chaque entraînement enregistre automatiquement (via `mlflow.autolog()`) les hyperparamètres (taille de vocabulaire, layers...), le temps d'exécution et les métriques de performance (Accuracy, F1-score).
- **Centralisation** : Les modèles sont versionnés et stockés dans un artifact store structuré, permettant de facilement revenir en arrière ou sélectionner le modèle "Champion".

### B. Déploiement Continu (CI/CD)
- Le code source est hébergé et versionné sur **GitHub**.
- Nous avons encapsulé notre logique d'inférence (récupérée par notre modèle Keras) dans une **API REST développée avec FastAPI**.
- Grâce aux **tests unitaires** automatisés, à chaque `commit`, nous certifions que l'API renvoie bien les prédictions attendues ("sad" ou "happy") sans régression.

### C. Hébergement sur le Cloud
Le cœur du MVP est hébergé sur le Cloud Microsoft Azure.
- Nous avons déployé notre **API sous forme d'une Azure Web App** (Instance Free F1). 
- Le script [test_api.py](file:///Users/j/Documents/OC_Inge_IA/Projet_7/test_api.py) confirme que l’endpoint `https://predictionsentiments-azepf7eme8dvftaa.francecentral-01.azurewebsites.net/feeling_predictions/{text}` répond avec succès en un temps très court avec le sentiment du tweet !

---

## 3. Supervision Continue avec Azure Application Insights

Un modèle en production, soumis aux nouvelles données du monde réel, a tendance à perdre en exactitude dans le temps: c'est le **Data Drift** (dérive des données). Pour y remédier :

### Traces et Alertes
Nous avons instrumenté le code de notre FastAPI ([main.py](file:///Users/j/Documents/OC_Inge_IA/Projet_7/Projet_7_API/main.py)) avec **OpenTelemetry et Azure Application Insights**.
- Chaque prédiction est tracée (ex: `logger.info(f"pour le texte {text}, la prediction est {feeling_result}")`) et envoyée à Azure.
- Cela nous offre un **dashboard de télémétrie** avec la latence de l'API, les erreurs HTTP, et surtout les logs de prédiction de notre modèle.
- **Alerting** : Des alertes (SMS/Email) sont configurables sur le portail Azure si un taux d'erreur 500 augmente ou si le volume de requêtes explose.

### Démarche d'Amélioration (Feedback Loop)
L'interface de test soumise aux utilisateurs nous permet de recueillir des informations primordiales en cas de fausse prédiction (quand l'utilisateur conteste le résultat du modèle). 
Ces "faux positifs/faux négatifs" sont eux aussi envoyés en traces. Périodiquement, cet échantillon d'échec est récupéré pour observer les termes problématiques et ré-entraîner le modèle (Active Learning), fermant ainsi la boucle vertueuse du MLOps.

---

## Conclusion

Ce prototype a prouvé la faisabilité technique de détecter les Bad Buzz via IA pour **Air Paradis**. Plus qu'une démonstration algorithmique, il s'agit d'un produit logiciel de Machine Learning robuste et monitoré, prêt à s'intégrer harmonieusement dans les systèmes d'alerte des équipes Marketing.
