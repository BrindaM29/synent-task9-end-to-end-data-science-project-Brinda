import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("Customer Churn Prediction")

gender = st.selectbox(
    "Gender",
    [0, 1]
)

senior = st.selectbox(
    "Senior Citizen",
    [0, 1]
)

tenure = st.number_input(
    "Tenure",
    0,
    100
)

monthly = st.number_input(
    "Monthly Charges",
    0.0,
    1000.0
)

total = st.number_input(
    "Total Charges",
    0.0,
    10000.0
)

if st.button("Predict"):

    sample = np.array([
        [
            gender,
            senior,
            tenure,
            monthly,
            total
        ]
    ])

    prediction = model.predict(sample)

    if prediction[0] == 1:
        st.error(
            "Customer likely to leave"
        )
    else:
        st.success(
            "Customer likely to stay"
        )
