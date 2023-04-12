import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

languages = {
    "German" : "DE",
    "English" : "EN",
    "Spanish" : "ES",
    "French" : "FR",
    "Japanese" : "JA",
    "Chinese" : "ZH"
}

dataframes = {}

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

for language in languages:
    __path__ = os.path.join(APP_ROOT, f"../static/reviews/analysed_amazon_reviews_multi_{languages[language]}.csv")
    with open(__path__, "r") as fCSV:
        df = pd.read_csv(fCSV)
        dataframes[language] = df


st.title("Sentiment Analysis in Amazon Reviews")

option = st.selectbox(
    'What language do you wish to select?',
    ('German', 'English', 'Spanish', 'French', 'Japanese', 'Chinese'))
st.header(f'Reviews in: {option}')
dfOption = dataframes[option]
dfOption['index'] = range(1, len(dfOption) + 1)
#st.bar_chart(dfOption, x='index', y=['compound'], height=500, use_container_width=True)
st.bar_chart(dataframes[option], x='stars', y='compound', height=500, use_container_width=True)
st.divider()
st.subheader("Example of a review with a classification of 5 stars")
fiveStarReview = dataframes[option].loc[dataframes[option]['stars'] == 5].sample(1)
if option == 'English':
    st.markdown("***Review text:*** " + fiveStarReview['review_text'].values[0])
else:
    st.markdown("***Review text:*** " + fiveStarReview['original_text'].values[0])
    st.markdown("***Translated text:*** " + fiveStarReview['review_text'].values[0])
st.markdown(f"***Positive score:*** `{fiveStarReview['pos'].values[0]}`")
st.markdown(f"***Negative score:*** `{fiveStarReview['neg'].values[0]}`")
st.markdown(f"***Neutral score:*** `{fiveStarReview['neu'].values[0]}`")
st.markdown(f"***Compound score:*** `{fiveStarReview['compound'].values[0]}`")
st.markdown(f"***Product category:*** `{fiveStarReview['product_category'].values[0]}`")
st.divider()
st.subheader("Example of a review with a classification of 1 star")
oneStarReview = dataframes[option].loc[dataframes[option]['stars'] == 1].sample(1)
if option == 'English':
    st.markdown("***Review text:*** " + oneStarReview['review_text'].values[0])
else:
    st.markdown("***Review text:*** " + oneStarReview['original_text'].values[0])
    st.markdown("***Translated text:*** " + oneStarReview['review_text'].values[0])
st.markdown(f"***Positive score:*** `{oneStarReview['pos'].values[0]}`")
st.markdown(f"***Negative score:*** `{oneStarReview['neg'].values[0]}`")
st.markdown(f"***Neutral score:*** `{oneStarReview['neu'].values[0]}`")
st.markdown(f"***Compound score:*** `{oneStarReview['compound'].values[0]}`")
st.markdown(f"***Product category:*** `{oneStarReview['product_category'].values[0]}`")
st.divider()

st.header("Aggregate Stats")
st.write("We aggregated the reviews from all languages and got the following stats:")
df = pd.DataFrame()
for lng in languages:
    df = pd.concat([df, dataframes[lng]])

meanCompound = df['compound'].mean()
meanCompound = round(meanCompound, 2)
st.write(f"***Mean compound score:*** `{meanCompound}`")
meanPos = df['pos'].mean()
meanPos = round(meanPos, 2)
st.write(f"***Mean positive score:*** `{meanPos}`")
meanNeg = df['neg'].mean()
meanNeg = round(meanNeg, 2)
st.write(f"***Mean negative score:*** `{meanNeg}`")
meanNeu = df['neu'].mean()
meanNeu = round(meanNeu, 2)
st.write(f"***Mean neutral score:*** `{meanNeu}`")
