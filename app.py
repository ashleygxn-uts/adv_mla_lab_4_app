import streamlit as st
from joblib import load
import pandas as pd

st.title('ML Streamlit App')

model = load('models/ada_reg.joblib')
scaler = load('models/scaler.joblib')

st.write("""
## The Machine Learning App

You can use this application in order to get predictions from a trained Adaboost model on the estimated number of shares for a news article.

You will have to select the values that describe a news article.
""")

