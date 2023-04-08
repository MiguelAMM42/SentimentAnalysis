import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
st.write(dataframes[option])
ax = sns.barplot(data=dataframes[option], x='stars', y='compound')
ax.set_title('Compound Score by Amazon Star Review')
fig = ax.get_figure()
st.pyplot(fig)

