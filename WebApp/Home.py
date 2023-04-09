import streamlit as st
import pandas as pd
from pathlib import Path

st.title("Sentiment Analysis of text")

st.header("You can consult the sentiment analysis of Amazon reviews in :")
# put links to the other pages
st.write("Reviews")


st.subheader("Made by:")
st.markdown("[Inês Vicente](https://github.com/inesvicente2001)")
st.markdown("[Jorge Melo](https://github.com/BatataDoc3)")
st.markdown("[Miguel Martins](https://github.com/MiguelAMM42)")

__path__ = Path("static/chatGPT_AI/processedData.csv")
with open(__path__) as fCSV:
    df = pd.read_csv(fCSV)
    st.write(df)


