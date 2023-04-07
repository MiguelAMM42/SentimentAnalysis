import streamlit as st
import pandas as pd

languages = {
    "German" : "DE",
    "English" : "EN",
    "Spanish" : "ES",
    "French" : "FR",
    "Japanese" : "JA",
    "Chinese" : "ZH"
}

dataframes = {}

for language in languages:
    with open(f"../Reviews/analysedData/analysed_amazon_reviews_multi_{languages[language]}.csv", "r") as fCSV:
        df = pd.read_csv(fCSV)
        dataframes[language] = df


st.write("REVIEWS")

option = st.selectbox(
    'What language do you wish to select?',
    ('German', 'English', 'Spanish', 'French', 'Japanese', 'Chinese'))
st.write('Reviews\' stats for: ', option)
#st.write(dataframes[option].head(10))
# plot with stars and negative/positive/compound values
st.line_chart(dataframes[option][["stars","neg","neu","pos","compound"]])