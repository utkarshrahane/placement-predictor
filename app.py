import streamlit as st
import pickle
import numpy as np

# Loading the model file (.pkl)
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🎓 Student Placement Predictor")

st.markdown("Enter the student's details below to predict if they will be placed.")

# Inputs from user
iq = st.number_input("🧠 IQ of the student:", min_value=0.0, step=1.0)
cgpa = st.number_input("📚 CGPA of the student:", min_value=0.0, max_value=10.0, step=0.1)

# Predict button

if st.button("🔍Predict"):
    # Convert inputs to 2D array for model
    input_features = np.array([[iq, cgpa]])
    result = model.predict(input_features)[0]

    if result == 1:
        st.success("✅ The student **will be placed**.")
    else:
        st.error("❌ The student **will not be placed**.")