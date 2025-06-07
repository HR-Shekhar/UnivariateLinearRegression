# app.py
import streamlit as st
import joblib

# Load model parameters (w and b)
params = joblib.load("model.pkl")
w = params["w"]
b = params["b"]

# App layout
st.set_page_config(page_title="Carbon Emission Predictor", page_icon="🌍", layout="centered")

# Title and description
st.title("🚗 Carbon Emission Predictor")
st.markdown("""
Enter the **engine size (in Litres)** of a vehicle, and this app will predict its **CO₂ emission (in grams/km)** using a Linear Regression model built from scratch.

This model was trained on real-world data without any ML library — powered by raw Python and math!
""")

# Input
engine_size = st.number_input("🔧 Engine Size (L)", min_value=0.0, max_value=10.0, step=0.1, format="%.2f")

# Predict
if st.button("Predict Emission"):
    emission = w * engine_size + b
    st.success(f"Estimated CO₂ Emission: **{emission:.2f} g/km**")

# Footer
st.markdown("---")
st.markdown("👨‍💻 Made by [Himanshu Shekhar](https://github.com/your-github-username) | Model built from scratch with 🧠 and ❤️")
