# Support de Présentation : Détection de Bad Buzz pour Air Paradis

*Note: Ce document regroupe le contenu à intégrer dans les slides PowerPoint pour la soutenance finale avec Mme Aline (Marketing Director, Air Paradis).*

---

## Slide 1 : Titre & Introduction
**Titre :** Anticipation des Bad Buzz sur les Réseaux Sociaux : Approche IA & Deep Learning
**Sous-titre :** Projet de Prototype pour Air Paradis par Marketing Intelligence Consulting (MIC)

**Points clés à l'oral :**
- Enjeu vital pour Air Paradis : protéger son image de marque en temps réel.
- Solution apportée : Un modèle d'Intelligence Artificielle de détection de sentiments (positif/négatif) sur les requêtes Twitter.

---

## Slide 2 : Démarche Méthodologique
**Titre :** Notre Méthodologie IA : De l'Exploration à la Production

**Contenu :**
1. **Acquisition & Nettoyage des Données** : Utilisation du jeu de données "Sentiment140" (tweets publics annotés).
2. **Phase de Modélisation Itérative** :
   - Modèle Baseline (Simple)
   - Modèle Deep Learning (Sur Mesure Avancé)
   - Expérimentation État de l'Art (BERT)
3. **Démarche MLOps** : Industrialisation du Machine Learning.
   - Suivi, Versioning, CI/CD, Déploiement Cloud et Monitoring.

---

## Slide 3 : Les Résultats des Modèles (Comparaison)
**Titre :** Comparaison des 3 Approches de Modélisation

**Tableau / Visuel :**
| Approche | Type de Modèle | Avantages | Inconvénients / Limites | Décision |
|----------|---------------|-----------|------------------------|----------|
| **1. Simple** | Régression Logistique / TF-IDF | Très rapide, très léger | Ne comprend pas le contexte ni la sémantique fine | *Baseline (référence)* |
| **2. Avancé (Choisi)** | Réseau de Neurones Keras + Embedding | Bonne capture sémantique, rapide à l'inférence | Temps d'entraînement moyen | **Sélectionné pour la PROD** |
| **3. État de l'art** | Transformer / BERT | Performances maximales | Trop lourd/coûteux pour un hébergement gratuit | *Écarté pour le MVP* |

**Points clés à l'oral :**
- Le modèle 2 (Advanced) offre le meilleur ratio Performance/Coût d'hébergement.

---

## Slide 4 : Suivi des Expérimentations (MLFlow)
**Titre :** MLOps : Suivi et Centralisation avec MLFlow

**Visuels (À inclure dans le PPT final) :**
- [Capture d'écran de l'UI MLflow listant les "Runs"]
- [Capture d'écran du détail d'un Run (Accuracy, Hyperparamètres)]

**Points clés à l'oral :**
- **Traçabilité** : Chaque entraînement est sauvegardé automatiquement.
- **Reproductibilité** : Fini les fichiers perdus. Tout est tracé pour le travail en équipe.

---

## Slide 5 : Déploiement en Production (CI/CD & API)
**Titre :** Une API Prête à l'Usage sur le Cloud

**Contenu :**
- **Code Géré sur GitHub** :
    - *[Insérer Capture d'écran des commits GitHub et structure de dossier Projet_7]*
    - **Lien GitHub** : *[Votre_Lien_Git]*
- **Tests Unitaires (CI/CD)** :
    - *[Insérer Capture d'écran de l'exécution réussie de test_api.py (Automatisé)]*
- **Déploiement Cloud (Azure)** :
    - L'API (FastAPI) a été déployée sur l'offre gratuite globale d'Azure.
    - Elle répond aux requêtes en quelques millisecondes: `https://predictionsentiments-azepf7eme8dvftaa.francecentral-01.azurewebsites.net/feeling_predictions/{text}`.

---

## Slide 6 : Supervision du Modèle en Temps Réel
**Titre :** Monitoring Actif avec Azure Application Insights

**Visuels (À inclure dans le PPT) :**
- [Capture d'écran d'Application Insights montrant les requêtes reçues et la latence]
- [Capture d'écran de la trace des prédictions ex: `prediction: happy/sad`]
- [Capture d'écran d'une alerte configurée "Si Erreurs Serveur > 3"]

**Points clés :**
- **Visibilité totale** : On sait ce que le modèle prédit sur les vrais tweets.
- **Alertes** : Si l'API ou le modèle tombe en panne (ou se met à faillir massivement), nous sommes notifiés.
- **Amélioration Continue** : Les mauvais signalements sont enregistrés pour ré-entraîner le modèle à terme.

---

## Slide 7 : Démonstration Fonctionnelle
**Titre :** Démo : Envoi d'un Tweet Live !

**Éléments pour la démo en live ou en vidéo enregistrée :**
- "I just got a promotion at work and I am thrilled!" -> Prédiction API -> **HAPPY**
- "My flight got canceled and I missed my best friend's wedding." -> Prédiction API -> **SAD**

*(Rappel : La soutenance requiert un enregistrement de cette démonstration pour éviter les coûts d'hébergement continus à l'étudiant).*

---

## Slide 8 : Conclusion
**Titre :** Prêt pour la Prochaine Étape

**Points de conclusion :**
- On a prouvé techniquement qu'un système de détection fonctionnait.
- L'architecture MLOps permet une mise à l'échelle future sécurisée.
- L'utilisation de ressources gratuites (Azure F1) valide l'approche MVP sans budget démesuré.

**Questions - Réponses.**
