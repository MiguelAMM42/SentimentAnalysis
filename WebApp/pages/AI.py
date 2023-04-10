import streamlit as st
import pandas as pd
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

__path__ = os.path.join(APP_ROOT, "../static/chatGPT_AI/processedData.csv")

st.write("A statistical analysis of the sentiments manifested about AI and ChatGPT")

with open(__path__, "r") as fCSV:
    df = pd.read_csv(fCSV)
    df['index'] = range(1, len(df) + 1)


weeks = df['week'].unique().tolist()
option = st.selectbox(
    'What week do you wish to select?',
    weeks)

st.header(f'Sentiment Analysis in Week: {option}')
#pensar no index
st.line_chart(df.loc[df['week'] == option], x='index', y='compound', height=500, use_container_width=True)


