# app.py
import streamlit as st
import joblib
import numpy as np

# Load both models
scratch = joblib.load("model.pkl")  # {'w': ..., 'b': ...}
sk_model = joblib.load("model_SL.pkl")  # LinearRegression()

# Page setup
st.set_page_config(page_title="Compare Carbon Emission Models", page_icon="⚖️", layout="centered")
st.title("⚖️ Compare CO₂ Emission Predictions")

st.markdown("""
This app compares CO₂ emission predictions made by:
- **Model A**: Built from scratch (manual gradient descent)
- **Model B**: Trained using `scikit-learn`  
   
Input the engine size to see how both models perform!
""")

# Input
x = st.number_input("Enter Engine Size (Litres)", min_value=0.0, max_value=10.0, step=0.1)

if st.button("Compare Predictions"):
    # Prediction using scratch model
    w, b = scratch["w"], scratch["b"]
    pred_scratch = w * x + b

    # Prediction using sklearn
    pred_sklearn = sk_model.predict(np.array([[x]]))[0]

    # Show results
    st.subheader("🔍 Results")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Scratch Model Prediction", value=f"{pred_scratch:.2f} g/km", delta=None)

    with col2:
        st.metric(label="scikit-learn Prediction", value=f"{pred_sklearn:.2f} g/km", delta=None)

# Footer
st.markdown("---")
st.markdown("Built by **Himanshu Shekhar** — One model from scratch, one from scikit-learn ❤️")
