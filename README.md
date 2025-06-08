# UnivariateLinearRegression
This is my first model which i trained with two different approaches.
First approach is the mathematical approach in which I wrote all the Cost funtion, Gradient and Gradient Descent to train my model.
And then I went with the regular approach of using the scikit-learn library.
I took the data from Kaggle, cleaned it and prepared it to use it for my Univariate Linear Regression.

# 📈 Univariate Linear Regression: From Scratch vs Scikit-learn

This project demonstrates a simple linear regression model trained from scratch using NumPy compared with the same model built using scikit-learn. The model predicts **Carbon Emissions** based on **Engine Size**.

## 📊 Model Details

- **From Scratch:** Manual gradient descent for parameter optimization
- **Scikit-learn:** `LinearRegression` from `sklearn.linear_model`
- **Target:** CO₂ Emissions (g/km)
- **Feature:** Engine Size (L)

## 🚀 Try the Web App

Compare predictions live on Streamlit:

🔗 [Launch App](https://enginesizevsco2emission.streamlit.app)

## 📁 Files Included

- `Univariate_Linear_Regression.ipynb`: Jupyter Notebook implementation
- `app.py`: Streamlit app comparing both models
- `requirements.txt`: Python dependencies

## 🔧 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## ✅ Built by

**Himanshu Shekhar** – Exploring machine learning principles.
