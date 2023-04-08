import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.write("A statistical analysis of the sentiments manifested about AI and ChatGPT")

with open(f"data/chatGPT_AI/processedData.csv", "r") as fCSV:
    df = pd.read_csv(fCSV)
    df['index'] = range(1, len(df) + 1)
    dfCopy = df.copy()
    dfCopy.drop(columns=['index'],inplace=True)
    st.write(dfCopy)

st.write("Sentiment Analysis")
st.line_chart(data=df, x="index", y="compound", use_container_width=True)

