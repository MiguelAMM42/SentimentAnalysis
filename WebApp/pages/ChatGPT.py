import streamlit as st
import pandas as pd

with open(f"Twitter_ChatGPT_AI/processed_data.csv", "r") as fCSV:
    df = pd.read_csv(fCSV)
    st.write(df)