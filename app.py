# app.py
import streamlit as st
import joblib
import numpy as np

# Load trained parameters
params = joblib.load("model.pkl")
w = params["w"]
b = params["b"]

st.title("Engine Size v/s CO2 emission")

# Input
x_input = st.number_input("Enter engine size:")

# Prediction
if st.button("Predict"):
    y_pred = w * x_input + b
    st.success(f"CO2 emission by the engine: {y_pred:.2f}")