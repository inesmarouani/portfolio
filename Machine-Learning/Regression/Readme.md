# Prédiction des Calories Brûlées

## Description du projet
Ce projet a pour objectif de développer un modèle d’intelligence artificielle capable de **prédire automatiquement le nombre de calories brûlées lors d’une activité physique**. Il fournit une estimation fiable de la dépense énergétique à partir de données physiologiques et de paramètres d’exercice, afin d’aider au suivi sportif et à l’optimisation des programmes d’entraînement.

---

## Objectif
Construire un **modèle de régression performant** pour estimer avec précision la quantité de calories dépensées. Les prédictions sont personnalisées selon les caractéristiques individuelles et les mesures enregistrées durant l’activité.

---

## Type de données
Le projet utilise des données tabulaires comprenant :

- Âge, sexe, taille et poids de l’individu  
- Durée de l’exercice  
- Fréquence cardiaque moyenne pendant l’activité  
- Température corporelle  
- Nombre de calories brûlées (**variable cible continue**)

---

## Contexte métier
L’évaluation précise de la dépense énergétique est essentielle pour :

- Les sportifs et coachs  
- Les applications de fitness  
- La gestion du poids et du suivi nutritionnel  

Les calculs traditionnels sont souvent approximatifs et peu personnalisés. L’automatisation via l’IA permet d’obtenir des estimations précises adaptées au profil de chaque utilisateur.

---

## Objectif final

- **Problème traité :** Régression (prédiction d’une valeur continue : calories brûlées)  
- **Évaluation :** RMSE, MAE et R²  
- **Livrable :** Un modèle prédictif pouvant être intégré dans une application fitness, un outil de coaching sportif ou un tableau de bord énergétique personnalisé.

---

## Étapes du projet

### 1. Collecte et chargement des données
- Importation des datasets CSV (`calories.csv` et `exercise.csv`)  
- Vérification des colonnes et types de variables  
- Aperçu des données, valeurs manquantes et doublons  

> Toutes les données sont complètes et aucune valeur aberrante n’a été détectée.

### 2. Analyse exploratoire des données (EDA)
- Distribution des variables numériques : âge, taille, poids, durée, fréquence cardiaque, température corporelle  
- Analyse de la variable cible (calories brûlées)  
- Comparaison hommes/femmes  
- Corrélations entre variables et variable cible  

**Observations clés :**
- Variables les plus corrélées aux calories : `Duration`, `Heart_Rate`, `Body_Temp`  
- Poids et taille influencent également la dépense énergétique  
- L’âge a peu d’impact  
- Quelques outliers à traiter dans `Weight`, `Body_Temp` et `Calories`

### 3. Préparation des données
- Encodage de la variable catégorielle `Gender` (One-Hot)  
- Standardisation robuste (`RobustScaler`) pour limiter l’impact des outliers

### 4. Modélisation
Modèles testés :

| Modèle | MAE | RMSE | R² | Performance |
|--------|-----|------|----|------------|
| Linear Regression | 8.44 cal | 11.49 cal | 0.967 | Bon |
| Random Forest | 1.81 cal | 2.81 cal | 0.998 | **Excellent** |
| Gradient Boosting | 2.61 cal | 3.61 cal | 0.997 | Très bon |

**Comparaison graphique :**
- Prédictions vs valeurs réelles  
- Distribution des erreurs  

---

## Analyse des modèles

### Linear Regression
- Erreur moyenne : 8.44 cal  
- R² : 0.967  
- Usage : prototype ou POC, non adapté à un usage professionnel

### Random Forest (**modèle recommandé**)
- Erreur moyenne : 1.81 cal  
- R² : 0.998  
- Usage : applications fitness premium, coaching professionnel, suivi nutritionnel médical

### Gradient Boosting
- Erreur moyenne : 2.61 cal  
- R² : 0.997  
- Usage : alternative mobile ou applications grand public

---

## Conclusion et recommandations
- **Random Forest** : meilleure précision, recommandé pour déploiement professionnel  
- **Gradient Boosting** : excellent compromis performance/ressources pour wearables et applications mobiles  
- **Linear Regression** : suffisant pour un prototype mais pas pour un usage précis  

Le projet démontre qu’il est possible d’obtenir des prédictions très fiables (<2 cal d’erreur) pour le suivi énergétique personnalisé.

---

## Technologies et librairies utilisées
- Python 3.x  
- pandas, numpy  
- matplotlib, seaborn, plotly  
- scikit-learn (LinearRegression, RandomForestRegressor, GradientBoostingRegressor, RobustScaler)  

---

## Comment exécuter le projet
1. Cloner le repo :  
```bash
git clone https://github.com/<votre-utilisateur>/<nom-du-repo>.git

**Auteur**
Ines Marouani
Contact : ines.marouani69@gmail.com
Projet réalisé dans le cadre de l’analyse de données et IA appliquée au sport
