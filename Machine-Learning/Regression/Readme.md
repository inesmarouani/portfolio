# 🍎 Burned Calories Prediction

[![Python](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## 📌 Description

This project implements a **regression model** to predict the number of **calories burned** during physical activities based on physiological and behavioral variables.
The goal: provide an **accurate and personalized estimate** for each individual—useful for health monitoring, sports coaching, and nutritional analysis.

---

## 🎯 Objectives

* Predict the number of calories burned based on: age, gender, weight, height, heart rate, activity duration, etc.
* Identify the most influential factors affecting caloric expenditure.
* Provide a usable model for sports or connected health applications.

---

## 🗂️ Dataset

| Variable     | Description                       |
| ------------ | --------------------------------- |
| `Gender`     | Individual’s gender               |
| `Age`        | Age in years                      |
| `Height`     | Height in cm                      |
| `Weight`     | Weight in kg                      |
| `Duration`   | Duration of activity (minutes)    |
| `Heart_Rate` | Average heart rate                |
| `Body_Temp`  | Body temperature                  |
| `Calories`   | Calories burned (target variable) |

> **Note**: Dataset is complete and cleaned, with no duplicates or missing values.

---

## 🔍 Exploratory Data Analysis (EDA)

* Distribution of variables and outlier detection
* Correlations between calories and other variables
* Visualizations: histograms, boxplots, scatter plots
* Observation: `Duration`, `Heart_Rate`, and `Weight` have a significant impact on calories burned

---

## ⚙️ Data Preparation

* Encoding `Gender` as a numerical variable (0/1)
* Standardization/normalization of features when needed
* Separation into **features / target** (`X` and `y`)
* **Train/test split** (e.g., 80% train / 20% test)

---

## 🧩 Modeling

* Algorithms used:

  * **Linear Regression**
  * **Random Forest Regressor**
  * **Gradient Boosting Regressor**

* Evaluation metrics:

  * **RMSE** (Root Mean Squared Error)
  * **R² Score** (coefficient of determination)
  * **MAE** (Mean Absolute Error)

### Example:

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Random Forest model
rf = RandomForestRegressor(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

# Evaluation
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)
print(f"RMSE: {rmse:.2f}, R²: {r2:.2f}")
```

---

## 📊 Results

* The Random Forest model provides the **best performance** on the dataset
* R² ≈ 0.85 → reliable predictions
* Most influential variables: `Duration`, `Heart_Rate`, `Weight`
* Visualizations: real vs predicted scatter plot, feature importance

---

## 🛠️ Technologies and Libraries

* **Language**: Python 3.x
* **Data manipulation & analysis**: Pandas, NumPy
* **Visualization**: Matplotlib, Seaborn, Plotly
* **Machine Learning**: Scikit-learn (`LinearRegression`, `RandomForestRegressor`, `GradientBoostingRegressor`)
* **Evaluation**: RMSE, MAE, R² metrics

---

## 📈 Conclusion

* The model allows for **accurate prediction** of calories burned during physical activities.
* Results can be used for: sports tracking, nutritional recommendations, connected health applications.
* The identified key variables help **understand the factors influencing caloric expenditure** and enable personalized training programs.


