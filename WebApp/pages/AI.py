import streamlit as st
import pandas as pd
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

__path__ = os.path.join(APP_ROOT, "../static/chatGPT_AI/processedData.csv")

#__path__ = Path("static/chatGPT_AI/processedData.csv")
st.write("A statistical analysis of the sentiments manifested about AI and ChatGPT")

with open(__path__, "r") as fCSV:
    df = pd.read_csv(fCSV)
    df['index'] = range(1, len(df) + 1)
    dfCopy = df.copy()
    dfCopy.drop(columns=['index'],inplace=True)
    st.write(dfCopy)

st.write("Sentiment Analysis")
st.line_chart(data=df, x="index", y="compound", use_container_width=True)

