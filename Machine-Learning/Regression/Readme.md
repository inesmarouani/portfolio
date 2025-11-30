# 🍎 Prédiction des Calories Brûlées

[![Python](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## 📌 Description

Ce projet met en œuvre un **modèle de régression** pour prédire le nombre de **calories brûlées** lors d’activités physiques en fonction de variables physiologiques et comportementales.
L’objectif : fournir une **estimation précise et personnalisée** pour chaque individu, utile pour le suivi santé, le coaching sportif et l’analyse nutritionnelle.

---

## 🎯 Objectifs

* Prédire le nombre de calories brûlées selon : âge, sexe, poids, taille, fréquence cardiaque, durée d’activité, etc.
* Identifier les facteurs les plus influents sur la dépense calorique.
* Fournir un modèle exploitable pour des applications sportives ou de santé connectée.

---

## 🗂️ Données utilisées

| Variable     | Description                        |
| ------------ | ---------------------------------- |
| `Gender`     | Sexe de l’individu                 |
| `Age`        | Âge en années                      |
| `Height`     | Taille en cm                       |
| `Weight`     | Poids en kg                        |
| `Duration`   | Durée de l’activité (minutes)      |
| `Heart_Rate` | Fréquence cardiaque moyenne        |
| `Body_Temp`  | Température corporelle             |
| `Calories`   | Calories brûlées (cible à prédire) |

> **Remarque** : Données complètes et nettoyées, sans doublons ni valeurs manquantes.

---

## 🔍 Analyse exploratoire (EDA)

* Distribution des variables et identification des outliers
* Corrélations entre calories et autres variables
* Visualisations : histogrammes, boxplots, scatter plots
* Observation : `Duration`, `Heart_Rate` et `Weight` ont un impact significatif sur les calories brûlées

---

## ⚙️ Préparation des données

* Encodage de `Gender` en variable numérique (0/1)
* Standardisation / normalisation des features si nécessaire
* Séparation **features / target** (`X` et `y`)
* Split **train/test** (ex. 80% train / 20% test)

---

## 🧩 Modélisation

* Algorithmes utilisés :

  * **Régression linéaire**
  * **Random Forest Regressor**
  * **Gradient Boosting Regressor**
* Métriques d’évaluation :

  * **RMSE** (Root Mean Squared Error)
  * **R² Score** (coefficient de détermination)
  * **MAE** (Mean Absolute Error)

### Exemple :

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Modèle Random Forest
rf = RandomForestRegressor(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

# Évaluation
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)
print(f"RMSE: {rmse:.2f}, R²: {r2:.2f}")
```

---

## 📊 Résultats

* Modèle Random Forest donne la **meilleure performance** sur le dataset
* R² ≈ 0.85 → prédictions fiables
* Variables les plus influentes : `Duration`, `Heart_Rate`, `Weight`
* Visualisations : scatter plot réel vs prédiction, feature importance

---

## 🛠️ Technologies et bibliothèques

* **Langage** : Python 3.x
* **Manipulation et analyse** : Pandas, NumPy
* **Visualisation** : Matplotlib, Seaborn, Plotly
* **Machine Learning** : Scikit-learn (`LinearRegression`, `RandomForestRegressor`, `GradientBoostingRegressor`)
* **Évaluation** : metrics RMSE, MAE, R²

---

## 📈 Conclusion

* Le modèle permet de **prédire avec précision** les calories brûlées lors d’activités physiques.
* Les résultats peuvent servir à : suivi sportif, recommandations nutritionnelles, applications de santé connectée.
* Les variables clés identifiées aident à **comprendre les facteurs influençant la dépense calorique** et à personnaliser les programmes sportifs.
