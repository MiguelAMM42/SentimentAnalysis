import streamlit as st
import pandas as pd

with open(f"../Twitter/data/chatGPT_AI/processedData.csv", "r") as fCSV:
    df = pd.read_csv(fCSV)
    st.write(df)