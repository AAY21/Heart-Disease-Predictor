# Heart-Disease-Predictor
Analysing the risk of Heart Disease

This repository contains a dataset, a Jupyter Notebook, and a deployment-ready app for predicting heart disease occurrence using machine learning techniques.
The goal of this project is to analyze patient health records and develop a model that can assist in early detection of heart disease risk.

---
# Repository Structure
heart.csv — The dataset used for training and evaluation.
Heart Disease Prediction System.ipynb — Jupyter Notebook containing data preprocessing, exploratory data analysis (EDA), and model building.
Model_joblib_heart.pkl — Saved machine learning model for prediction.
heart_app.py — Web app (Flask/Streamlit) for real-time prediction.
README.md — Project documentation.
LICENSE — License for open-source usage.

---
# Features
Data Cleaning and Preprocessing
Exploratory Data Analysis (EDA) with visualizations
Feature selection and transformation
Machine Learning model training and evaluation
Deployment-ready web app for predictions

---
# Technologies Used
Python 3.x
Jupyter Notebook
Pandas, NumPy
Matplotlib, Seaborn
Scikit-learn
Joblib (for model persistence)
Streamlit (for deployment)

---
# Models Used
The following machine learning models were implemented and compared:
Logistic Regression
Support Vector Machine
KNearestNeighbour(KNN)
Decision Tree Classifier
Random Forest Classifier
GradientBoosting Classifier

Performance metrics (Accuracy, Precision, Recall, F1-score, ROC-AUC) were used to evaluate the models and determine the most effective approach for heart disease prediction.

---
# Dataset

The dataset (heart.csv) includes patient information such as:
Age
Gender
Chest Pain Type
Resting Blood Pressure
Cholesterol Level
Fasting Blood Sugar
Resting ECG
Max Heart Rate
Exercise-Induced Angina
Oldpeak (ST depression)
ST slope
Target Variable: target (1 = Heart Disease, 0 = No Heart Disease)

---
# How to Run
Clone the repository:
git clone https://github.com/your-username/heart-disease-prediction.git
cd heart-disease-prediction

---
Install dependencies:
pip install -r requirements.txt

Run the Jupyter Notebook for training and evaluation:
jupyter notebook "Heart Disease Prediction System.ipynb"

Run the web app:
streamlit run heart_app.py

This project demonstrates how machine learning can help in predicting critical health risks like heart disease, assisting in early intervention and better healthcare decisions.
