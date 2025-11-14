# 🕵️‍♂️ Crime Incidents in 2024 — Machine Learning Project

This project performs a full end-to-end analysis of crime incident data from 2024 and develops machine learning models to understand crime patterns, trends, and predictive insights.
It includes dataset preprocessing, exploratory data analysis, visualizations, and ML-based classification/regression modeling.

---

## 📁 Project Files

```
crime_incidents_in_2024/
│
├── Crime_Incidents_in_2024.csv                 # Raw dataset
├── crim_analyzed.csv                           # Cleaned / processed dataset
├── Data_Analysis&Machine_Learning_Project_.ipynb # Main notebook for data analysis + ML
├── crime_analysis.py                           # Python script for ML workflow
├── README.md                                   # Documentation
```

---

## 📊 Project Overview

The goal of this project is to understand crime activity patterns in 2024 and build predictive machine learning models.

### Includes:

* Data cleaning (missing values, duplicates, outliers)
* Feature engineering (time-based features, location encoding, etc.)
* Exploratory data analysis
* Visual insights using Matplotlib/Seaborn/Pandas
* ML model training + evaluation
* Prediction on processed crime datasets
* Exported and cleaned data (`crim_analyzed.csv`)
* Reusable analysis script (`crime_analysis.py`)

---

## 🧹 Data Preprocessing

Key preprocessing steps implemented:

* Formatting timestamps
* Encoding categorical variables
* Removing null or corrupted entries
* Detecting and handling outliers
* Creating new analytical features
* Splitting data for ML training/testing

---

## 🔍 Exploratory Analysis (EDA)

The notebook produces multiple visual analyses:

* Crime frequency by time (hour/day/month)
* Crime type distribution
* Location hotspots
* Correlation heatmaps
* Trend patterns throughout the year

These insights help identify high-risk time frames and areas.

---

## 🤖 Machine Learning Models

Models commonly used in the notebook:

* Random Forest
* Logistic Regression
* XGBoost / Gradient Boosting
* Decision Trees
* KNN
* Naive Bayes

Evaluation metrics:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion matrix
* ROC curves

The best-performing model can then be used for predictions.

---

## ▶️ Running the Analysis Script

To run the Python script version:

```bash
python crime_analysis.py
```

This will:

* Load dataset
* Preprocess data
* Train ML models
* Output evaluation metrics

---

## 🔬 Running the Notebook

```bash
jupyter notebook
```

Open:

```
Data_Analysis&Machine_Learning_Project_.ipynb
```

Run all cells to execute full workflow:

1. Load raw data
2. Clean + preprocess
3. Analyze
4. Train ML models
5. Export cleaned dataset

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/FouaadAI/crime_incidents_in_2024.git
cd crime_incidents_in_2024
```

### 2. Install dependencies

Typical libraries used:

```
pandas
numpy
matplotlib
seaborn
scikit-learn
xgboost
```

If you want, I can generate a **requirements.txt** file automatically.

---

## 📈 Results

Depending on the ML pipeline, results include:

* Crime prediction accuracy
* Performance comparison across multiple algorithms
* Time-based crime forecast
* Identification of high-risk zones
* Clean dataset saved as `crim_analyzed.csv`

---

## 📘 Future Improvements

* Build a Streamlit dashboard
* Deploy as a crime prediction API
* Add geospatial insights with Folium
* Train deep learning models for advanced forecasting

---

## 📝 License

This project is under the MIT License.
Feel free to use and modify for research or development.

---
