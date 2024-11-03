import streamlit as st
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import RidgeClassifier
import pickle

# Load pre-trained model and transformer
model_pipeline = pickle.load(open("estimator1.pkl", "rb"))

st.title("Bank Marketing Prediction")
st.subheader("By Md Mujahid Ahmed")

# Load the dataset
data = pd.read_csv("Cleaned dataset of marketing.csv")

# Title of the app
st.title("Marketing Dataset Analysis")

# Display the dataset
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(data)

# Display basic statistics
if st.checkbox("Show statistics"):
    st.subheader("Statistics")
    st.write(data.describe())

# Create a sidebar for user inputs
st.sidebar.header("User Input Features")
# Define the inputs for prediction, ensuring all required columns are present
age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=32)
balance = st.sidebar.number_input("Balance", min_value=-10000, max_value=100000, value=1000)
housing = st.sidebar.selectbox("Housing", options=[0, 1])
contact = st.sidebar.selectbox("Contact Type", options=['cellular', 'unknown', 'telephone'])
day = st.sidebar.number_input("Day", min_value=1, max_value=31, value=20)
duration = st.sidebar.number_input("Duration (minutes)", min_value=0.0, max_value=60.0, value=2.0, step=0.01)
campaign = st.sidebar.number_input("Campaign", min_value=1, max_value=100, value=1)
previous = st.sidebar.number_input("Previous Contacts", min_value=0, max_value=50, value=0)
poutcome = st.sidebar.selectbox("Previous Outcome", options=['unknown', 'failure', 'other', 'success'])
balance_housing = st.sidebar.number_input("Balance Housing", min_value=-10000, max_value=100000, value=0)

# Collect inputs in the correct format for prediction
data = pd.DataFrame({
    'age': [age],
    'balance': [balance],
    'housing': [housing],
    'contact': [contact],
    'day': [day],
    'duration': [duration],
    'campaign': [campaign],
    'previous': [previous],
    'poutcome': [poutcome],
    'balance_housing': [balance_housing]
})

if st.button("Predict"):
    try:
        # Make prediction using the loaded model pipeline
        prediction = model_pipeline.predict(data)
        st.write("Prediction:", prediction[0])  # Display prediction directly
    except Exception as e:
        st.error(f"Error during prediction: {e}")

