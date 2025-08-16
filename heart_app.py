import streamlit as st
import joblib
import numpy as np

# Load trained model (update filename if needed)
model = joblib.load("Model_joblib_heart")

# Page settings
st.set_page_config(page_title="❤️ Heart Disease Prediction", layout="centered")
st.title("❤️ Heart Disease Prediction System")
st.write("Fill in the details below to predict heart disease risk.")

# Input fields (equivalent to Tkinter entries)
age = st.number_input("Enter Your Age", min_value=1, max_value=120, value=30)
sex = st.selectbox("Male or Female (1 = Male, 0 = Female)", [1, 0])
cp = st.number_input("Enter Value of CP (Chest Pain Type)", min_value=0, max_value=3, value=0)
trestbps = st.number_input("Enter Value of Trestbps (Resting BP)", min_value=80, max_value=200, value=120)
chol = st.number_input("Enter Value of Chol (Cholesterol)", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Enter Value of FBS (Fasting Blood Sugar > 120 mg/dl)", [0, 1])
restecg = st.number_input("Enter Value of restecg (Rest ECG)", min_value=0, max_value=2, value=1)
thalach = st.number_input("Enter Value of thalach (Max Heart Rate)", min_value=60, max_value=220, value=150)
exang = st.selectbox("Enter Value of exang (Exercise Angina)", [0, 1])
oldpeak = st.number_input("Enter Value of oldpeak (ST Depression)", min_value=0.0, max_value=10.0, value=1.0)
slope = st.number_input("Enter Value of slope (Slope of Peak Exercise)", min_value=0, max_value=2, value=1)
ca = st.number_input("Enter Value of ca (Major Vessels)", min_value=0, max_value=4, value=0)
thal = st.number_input("Enter Value of thal", min_value=0, max_value=3, value=1)

# Collect all inputs into feature vector
features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                      thalach, exang, oldpeak, slope, ca, thal]])

# Prediction button
if st.button("🔍 Predict"):
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    if prediction == 1:
        st.error(f"⚠️ High Risk of Heart Disease! (Probability: {probability:.2f})")
    else:
        st.success(f"✅ Low Risk of Heart Disease. (Probability: {probability:.2f})")
