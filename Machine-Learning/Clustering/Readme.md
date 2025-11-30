# 🛍️ Segmentation Clientèle avec K-Means

[![Python](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## 📌 Description

Ce projet implémente un **modèle de clustering K-Means** pour segmenter automatiquement une base clients en groupes homogènes.
L’objectif : identifier des profils distincts afin de **mieux comprendre les clients**, personnaliser les offres et optimiser les campagnes marketing.

---

## 🎯 Objectifs

* Créer une segmentation **actionnable et cohérente**.
* Identifier des groupes selon : âge, revenu, score de dépense, comportement d’achat.
* Fournir une base pour : campagnes marketing ciblées, fidélisation, offres personnalisées.

---

## 🗂️ Données utilisées

| Variable                 | Description                             |
| ------------------------ | --------------------------------------- |
| `Gender`                 | Sexe du client                          |
| `Age`                    | Âge du client                           |
| `Annual Income (k$)`     | Revenu annuel en k$                     |
| `Spending Score (1-100)` | Score de dépense / comportement d’achat |

> **Remarque** : Données complètes, pas de valeurs manquantes ou doublons.

---

## 🔍 Analyse exploratoire (EDA)

* Distribution des variables et identification des outliers
* Corrélations entre âge, revenu et score de dépense
* Scatter matrix et pairplot pour visualiser les regroupements naturels
* Observation : Age, Income et Spending Score montrent des tendances bimodales → parfait pour K-Means

---

## ⚙️ Préparation des données

* Encodage de `Gender` en variable numérique (One-Hot)
* Standardisation avec `StandardScaler`
* Création du dataset final pour clustering

---

## 🧩 Clustering K-Means

* **Méthodes pour déterminer le nombre de clusters** :

  * Méthode du coude (Elbow Method)
  * Score de silhouette
  * Visualisations Yellowbrick
* **Nombre optimal de clusters** : `k = 3`

### Profils des clusters

| Cluster | Âge        | Revenu   | Score de dépense | Profil                                             |
| ------- | ---------- | -------- | ---------------- | -------------------------------------------------- |
| 0       | 20-40 ans  | 30-70 k$ | Élevé            | Jeunes consommateurs, forte dépense                |
| 1       | 20-40 ans  | 20-50 k$ | Modéré           | Jeunes, dépense prudente, sensibles aux promotions |
| 2       | 40-60+ ans | 100 k$+  | Faible           | Plus âgés, hauts revenus, achats ciblés            |

> **Remarque** : Quelques chevauchements naturels existent entre clusters, reflétant la continuité des comportements clients.

---

## 📊 Résultats

* Segmentation claire et exploitable
* Identification de profils stratégiques pour **marketing, fidélisation et offres premium**
* Visualisations : pairplot, diagrammes de densité, silhouettes

---

## 🛠️ Technologies et bibliothèques

* **Langage** : Python 3.x
* **Manipulation et analyse** : Pandas, NumPy
* **Visualisation** : Matplotlib, Seaborn, Plotly
* **Machine Learning** : Scikit-learn (`KMeans`, `StandardScaler`)
* **Évaluation clusters** : Yellowbrick

---

## 📈 Conclusion

La segmentation en **3 clusters** permet de :

1. Identifier les clients à forte dépense et jeunes (Cluster 0)
2. Travailler sur la fidélisation et montée en gamme (Cluster 1)
3. Proposer des offres premium ciblées aux hauts revenus peu dépensiers (Cluster 2)

Cette approche fournit une **base solide pour la stratégie marketing personnalisée** et peut être intégrée dans un CRM ou un tableau de bord analytique.

