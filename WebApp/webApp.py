import streamlit as st
import pandas as pd

st.write("Hello, World!")

with open("../Reviews/analysedData/analysed_amazon_reviews_multi_DE.csv", "r") as fCSV:
    df = pd.read_csv(fCSV)


st.write(df)
