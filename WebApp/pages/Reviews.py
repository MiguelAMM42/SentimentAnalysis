import streamlit as st
import pandas as pd

languages = {
    "de": "German",
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "ja": "Japanese",
    "zh": "Chinese"
}


st.write("REVIEWS")

option = st.selectbox(
    'What language do you wish to select?',
    ('German', 'English', 'Spanish'))

st.write('You selected:', option)


for language in languages.keys():
    st.write(f"Language: {languages[language]}")
    with open(f"../Reviews/analysedData/analysed_amazon_reviews_multi_{language.upper()}.csv", "r") as fCSV:
        df = pd.read_csv(fCSV)
    st.write(df)
