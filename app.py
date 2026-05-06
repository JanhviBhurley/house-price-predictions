import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

st.title("House Price Prediction")

area = st.number_input("Area (sq ft)")
rooms = st.number_input("Number of Rooms")
bathrooms = st.number_input("Bathrooms")

if st.button("Predict"):
    price = (area * 100) + (rooms * 50000) + (bathrooms * 30000)
    st.success(f"Estimated Price: ₹{price}")