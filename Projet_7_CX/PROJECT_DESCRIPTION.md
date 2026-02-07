# Sentiment Analysis using Deep Learning - Project Description

## 📋 Project Overview

**Duration:** 110 hours
**Status:** In Progress
**Client:** Air Paradis (Airline Company)
**Project Type:** AI Engineering - Prototype Development & MLOps Implementation

---

## 🎯 Project Context

You are an AI Engineer at **MIC (Marketing Intelligence Consulting)**, a consulting firm specializing in digital marketing challenges. Air Paradis airline company has commissioned your firm to create an AI product that can **anticipate negative buzz (bad buzz) on social media** by predicting sentiment associated with tweets.

**Deadline:** Presentation to Air Paradis marketing director (Mme Aline) in 2 weeks

---

## 📚 Learning Objectives

Throughout this project, you will:

### 1. **Develop AI Models**
   - Create sentiment prediction models from textual data using various approaches
   - Start with simple approaches (logistic regression)
   - Progress to deep neural networks with advanced techniques
   - Explore word embeddings (at least 2 different approaches)
   - Evaluate BERT model performance for sentiment analysis
   - Compare and select the best-performing approach for production

### 2. **Implement MLOps Methodology**
   - Understand MLOps principles and their importance for production deployment
   - **MLFlow Integration:**
     - Experiment tracking and reporting
     - Model management and versioning
     - Model serving capabilities
   - Continuous deployment pipeline
   - Automated unit testing
   - Performance monitoring in production

### 3. **Deploy to Production**
   - Build REST API for sentiment prediction
   - Deploy on free Cloud platform
   - Create local interface (Jupyter notebook or Streamlit app)
   - Implement monitoring with Azure Application Insights
   - Set up alerting system for model drift

### 4. **Communication & Documentation**
   - Create non-technical presentation for stakeholders
   - Write blog article showcasing your modeling approach and MLOps practices
   - Document methodology and results

---

## 📝 Requirements & Deliverables

### Core Requirements

#### 1. **Model Development - Two Approaches**

**Approach 1: Simple Custom Model**
- Develop a basic model (e.g., logistic regression)
- Quick prototype for rapid baseline
- Establishes comparison metric

**Approach 2: Advanced Custom Model** ⭐ **(For Production)**
- Deep neural network architecture
- Test minimum 2 different word embeddings
- Evaluate BERT model performance
- Select best performing approach for deployment
- Model must be deployable on free tier cloud platform

#### 2. **Data**
- **Dataset:** Sentiment140 (Twitter sentiment dataset)
- **Source:**
  - Kaggle: https://www.kaggle.com/kazanova/sentiment140
  - Direct download: https://s3-eu-west-1.amazonaws.com/static.oc-static.com/prod/courses/files/AI+Engineer/Project+7%C2%A0-+D%C3%A9tectez+les+Bad+Buzz+gr%C3%A2ce+au+Deep+Learning/sentiment140.zip
- **Data Description:** Tweet information (user, content, timestamp) + binary sentiment label (negative or not)

#### 3. **MLOps Pipeline**

**MLFlow Integration:**
- [ ] Experiment tracking and reporting
- [ ] Model centralization and versioning
- [ ] MLFlow serving testing

**Continuous Deployment:**
- [ ] Git + GitHub repository
- [ ] Automated unit tests
- [ ] Free Cloud platform deployment (Azure webapp F1, PythonAnywhere, Heroku student, etc.)
- [ ] CI/CD pipeline integration

**Production Monitoring:**
- [ ] Azure Application Insights setup
- [ ] Track mispredicted tweets (text + prediction)
- [ ] Alert system for anomalies:
  - Trigger SMS/email alert when >3 mispredictions occur within 5 minutes
  - Monitor model performance metrics
- [ ] Drift detection strategy

#### 4. **Deployment & API**
- [ ] REST API exposing the model
- [ ] Free tier cloud deployment
- [ ] Local interface (Jupyter notebook or Streamlit app)
- [ ] Input: Tweet text → Output: Sentiment prediction

#### 5. **Optimization (if needed)**
- If advanced model exceeds size limits:
  - Use TensorFlow Lite conversion
  - Or deploy simple model with comparable results
  - Document trade-offs

#### 6. **Documentation & Presentation**
- [ ] MLOps principles presentation (with non-technical audience in mind)
- [ ] Project methodology presentation
- [ ] Blog article on modeling approach and MLOps implementation
- [ ] Model performance summary

---

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Data Processing** | Python, Pandas, NumPy | Data loading, cleaning, preprocessing |
| **NLP** | NLTK, spaCy, Hugging Face | Text processing, tokenization, embeddings |
| **Model Development** | TensorFlow/Keras, PyTorch, scikit-learn | Model training and evaluation |
| **Word Embeddings** | Word2Vec, GloVe, FastText | (minimum 2 different approaches) |
| **Advanced Models** | BERT, Transformers | Performance evaluation |
| **MLOps** | MLFlow | Experiment tracking, model management |
| **Deployment** | Flask/FastAPI | REST API development |
| **Cloud Platform** | Azure (App Service F1) / Heroku / PythonAnywhere | Production hosting |
| **Monitoring** | Azure Application Insights | Performance tracking, alerting |
| **CI/CD** | GitHub Actions | Automated testing and deployment |
| **Frontend** | Streamlit or Jupyter | Local prediction interface |

---

## 📊 Project Phases

### Phase 1: Data Exploration & Preparation
- Load and explore Sentiment140 dataset
- Data cleaning and preprocessing
- Text tokenization and feature engineering
- Train/test split

### Phase 2: Simple Model Development
- Implement logistic regression baseline
- Evaluate and document performance
- Establish comparison metrics

### Phase 3: Advanced Model Development
- Implement neural network architecture
- **Word Embeddings Testing:**
  - Embedding 1 (e.g., Word2Vec, GloVe, FastText)
  - Embedding 2 (e.g., different from above)
  - Compare performance
- **BERT Evaluation:**
  - Test BERT performance
  - Document improvements
- Select best approach for production

### Phase 4: MLOps Implementation
- Set up MLFlow
- Track experiments and metrics
- Version and register models
- Test MLFlow serving

### Phase 5: Deployment & API
- Develop REST API (Flask/FastAPI)
- Deploy to free cloud platform
- Create local Streamlit/notebook interface
- Test end-to-end prediction pipeline

### Phase 6: Production Monitoring
- Configure Azure Application Insights
- Implement misprediction tracking
- Set up alerting mechanism
- Define model improvement strategy

### Phase 7: Presentation & Documentation
- Create stakeholder presentation
- Write technical documentation
- Write blog article
- Prepare client demo materials

---

## ✅ Success Criteria

1. **Models Deployed:** Both simple and advanced models trained and evaluated
2. **Best Model in Production:** Advanced model serving predictions via API
3. **MLOps Implementation:** Complete tracking, versioning, and monitoring
4. **Continuous Deployment:** Automated pipeline with tests
5. **Monitoring Active:** Alerts configured and tested
6. **Documentation Complete:** Presentations and blog article delivered
7. **Performance Target:** Acceptable sentiment prediction accuracy on test set
8. **Cost Efficient:** Running on free tier cloud platform

---

## 📌 Key Milestones

| Milestone | Deadline |
|-----------|----------|
| Data exploration & baseline model | Week 1 |
| Advanced models & embedding testing | Week 1.5 |
| MLFlow setup & experiment tracking | Week 2 |
| API deployment | Week 2 |
| Production monitoring setup | Week 2.5 |
| Presentation & documentation | Week 2.5 |
| **Client Presentation** | **Week 2** |

---

## 📦 Livrables et Soutenance

### 📋 Évaluation et Livrables

#### **Livrables à Remettre**

1. **API de Prédiction du Score** ⭐
   - Expose le "Modèle sur mesure avancé"
   - Déployée sur un service Cloud (Azure webapp, AWS, ou Heroku)
   - Reçoit en entrée un tweet
   - Retourne le sentiment associé au tweet prédit par le modèle
   - Lien vers l'API sur le Cloud requis

2. **Scripts et Notebooks de Modélisation**
   - Ensemble complet des scripts pour les trois approches:
     - Approche classique (logistic regression)
     - Modèle sur mesure avancé (neural network)
     - Modèle avancé BERT
   - Intégration MLFlow:
     - Tracking des expérimentations
     - Enregistrement des modèles

3. **Dossier de Code Versionné**
   - Géré via Git/GitHub
   - Contenu:
     - Notebooks des modélisations avec MLFlow tracking
     - Code de déploiement du modèle sous forme d'API
     - Fichier introductif (README): objectif du projet et découpage des dossiers
     - Fichier des packages utilisés (requirements.txt)

4. **Interface de Test de l'API**
   - Exécutée en local (Jupyter notebook ou Streamlit)
   - Fonctionnalités:
     - Saisie d'un tweet par l'utilisateur
     - Affichage de la prédiction
     - Demande de validation de la pertinence de la prédiction
     - Envoi d'une trace à Azure Application Insight en cas de non-validation

5. **Article de Blog Technique**
   - **Longueur:** 1500 à 2000 mots + copies d'écrans
   - **Contenu requis:**
     - Présentation synthétique et comparaison des trois approches
     - Comparaison: "Modèle sur mesure simple" vs "Modèle sur mesure avancé" vs "Modèle avancé BERT"
     - Démarche MLOps implémentée:
       - Principes MLOps
       - Étapes mises en œuvre: tracking, stockage modèle, gestion version, tests unitaires, déploiement
       - Suivi de la performance en production: traces et alertes sur Azure Application Insights
       - Démarche d'analyse des statistiques et amélioration du modèle dans le temps

6. **Support de Présentation (PowerPoint)**
   - Démarche méthodologique
   - Résultats des différents modèles
   - Expérimentations MLFlow et visualisation via l'UI MLFlow
   - Mise en production du modèle avancé
   - Preuves documentées:
     - Copies écran des commits GitHub et structure du dossier
     - Lien vers le dossier GitHub
     - Exécution des tests unitaires (preuve du pipeline de déploiement continu)
     - Suivi de performance sur Azure Application Insight et déclenchement des alertes

#### **Format de Remise**

Dossier zip nommé: `Titre_du_projet_nom_prénom`

Contenant les livrables nommés ainsi:
- `Nom_Prénom_1_API_mmaaaa`
- `Nom_Prénom_2_scripts_notebook_modélisation_mmaaaa`
- `Nom_Prénom_3_dossier_code_mmaaaa`
- `Nom_Prénom_4_interface_test_API_mmaaaa`
- `Nom_Prénom_5_blog_mmaaaa`
- `Nom_Prénom_6_presentation_mmaaaa`

**Exemple:** `Dupont_Jean_1_API_012024`

---

### 🎤 Déroulement de la Soutenance

#### **Structure Générale**
- **Durée totale:** 30 minutes
- **Rôle de l'évaluateur:** Observateur neutre, pas de rôle spécifique
- Présentation complète de votre travail par l'étudiant

#### **1️⃣ Présentation (20 minutes)**

**Phase 1: Modélisation (8 minutes)**
- Élaboration du modèle selon l'approche "modèle sur mesure simple"
- Modèles de l'approche "modèle sur mesure avancé"
- Modèle avancé BERT
- Simulations et résultats préliminaires

**Phase 2: Comparaison des Résultats (5 minutes)**
- Résultats comparés des trois modèles
- Synthèse des principes du MLOps (1-2 slides)
- Démarche d'expérimentation avec MLFlow
- Tableau de synthèse des scores des modèles
- Visualisation des résultats détaillés via l'UI de MLFlow

**Phase 3: Mise en Production (7 minutes)**
- **Déploiement Continu:**
  - Démarche de déploiement en production sur le Cloud choisi
  - Moteur d'inférence via création d'une API

- **Démonstration Fonctionnelle:**
  - Appel au moteur d'inférence avec exemple de tweet
  - Démonstration du test pour déterminer sentiment positif/négatif

- **Suivi en Production:**
  - Présentation des traces et alertes sur Azure Application Insights
  - Synthèse d'une démarche d'analyse du suivi en production
  - Stratégie d'amélioration du modèle dans le temps

#### **2️⃣ Discussion (5 minutes)**
- L'évaluateur vous challengera sur vos choix techniques
- Questions sur les décisions prises
- Justification des approches choisies

#### **3️⃣ Débriefing (5 minutes)**
- Discussion constructive avec l'évaluateur
- Retours et conseils pour l'avenir

---

### ☁️ Solutions de Déploiement Cloud

Plusieurs solutions s'offrent à vous. **L'étudiant doit choisir celle qui convient le mieux à son contexte.**

#### **Important:** Enregistrement de la Démo
Lors de la soutenance, l'étudiant et l'évaluateur veilleront à **enregistrer la démonstration de l'application en production**. Cela permet au jury de visualiser la démo sans que l'étudiant ne doive maintenir l'application sur le Cloud, évitant ainsi des coûts inutiles.

#### **Option 1: Heroku**
- **Statut:** Devenu payant depuis fin novembre 2022
- **Coûts:** À votre charge
- **Obligation:** Aucune - vous n'êtes pas obligé de vous investir financièrement
- **Recommandation:** Si vous choisissez Heroku, les coûts seront minimes pour cette courte utilisation

#### **Option 2: Azure webapp** ✅ (Recommandé)
- **Coûts:** Gratuit dans les limites (1 Go)
- **Avantages:**
  - Intégration native avec Application Insights
  - Plan F1 gratuit disponible
  - Solution cohérente avec votre stack monitoring
- **Documentation:** FAQ disponible sur Azure App Service Free Tier

#### **Option 3: AWS**
- **Offre gratuite:** EC2 T2 Micro (1 Go) pendant 12 mois
  - 750 heures/mois (gratuit)
  - Après 12 mois: ~1,3 centimes €/heure (10€/mois)
- **Coûts pour ce projet:** Très limité (quelques heures/jours de test) = <1€
- **Documentation:**
  - Offre AWS Free Tier: https://aws.amazon.com/fr/free/
  - Types d'instances: https://aws.amazon.com/fr/ec2/instance-types/

---

## 💡 Important Notes

- **Audience Consideration:** Presentations must be understandable to non-technical stakeholders
- **Cost Efficiency:** Prioritize free/student tier cloud solutions
- **Model Size:** If deployment exceeds size limits, use TensorFlow Lite or simpler model
- **MLOps Focus:** Demonstrate MLOps value as new company priority
- **Performance Tracking:** Implement robust monitoring for real-world deployment
- **Blog Content:** Document lessons learned and methodology

---

## 📚 Resources

- **Dataset:** [Sentiment140 on Kaggle](https://www.kaggle.com/kazanova/sentiment140)
- **MLFlow Documentation:** https://mlflow.org
- **Azure Application Insights:** https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview
- **Deployment Platforms:**
  - [Azure App Service Free Tier](https://azure.microsoft.com/en-us/services/app-service/)
  - [Heroku Student Pack](https://www.heroku.com/github-students)
  - [PythonAnywhere](https://www.pythonanywhere.com)

---

## 🚀 Getting Started

1. **Understand the Requirements:** Read this document completely
2. **Take Notes:** Document your understanding of each component
3. **Review Phases:** Study the project phases and success criteria
4. **Prepare Questions:** List questions for your mentor sessions
5. **Set Up Repository:** Initialize Git repository with proper structure
6. **Begin Phase 1:** Start with data exploration

---

## 📞 Contact & Support

Manager: Marc (project oversight)
Client: Mme Aline, Air Paradis Marketing Director
Mentor: Available for guidance sessions

---

**Last Updated:** 2025-11-21
**Project Status:** Ready to Start
