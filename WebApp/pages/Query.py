import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
import re
import snscrape.modules.twitter as sntwitter
from tqdm import tqdm


def scraper(query, maxTweets):
    scraper = sntwitter.TwitterSearchScraper(query)
    data = scraper.get_items()

    tweets = []

    counter = 0

    for tweet in data:
        if counter > maxTweets:
            break
        if tweet.lang == 'en':
            text = tweet.renderedContent
            text = re.sub(',','\\,',text)
            text = re.sub('\n',' ',text)
            l = []
            l.append(tweet.id)
            l.append(tweet.date)
            l.append(text)
            l.append(tweet.likeCount)
            l.append(tweet.retweetCount)
            l.append(tweet.replyCount)
            l.append(tweet.hashtags)
            tweets.append(l)
            counter +=1

    df = pd.DataFrame(tweets, columns=['id', 'date', 'renderedContent', 'likeCount', 'retweetCount', 'replyCount', 'hashtags'])
    
    return df


def sentimentAnalysis(df):
    res = {}
    for i, row in df.iterrows():
        text = row['renderedContent']
        id = row['id']
        res[id] = sia.polarity_scores(text)

    sentiments = pd.DataFrame(res).T
    sentiments = sentiments.reset_index().rename(columns={'index': 'id'})
    sentiments = sentiments.merge(df, how='left')

    return sentiments

def processData(df):
    sentiments = sentimentAnalysis(df)
    return sentiments


def dropColumns(df,cols):
    df = df.drop(columns=cols)
    return df


st.write("A statistical analysis of the sentiments manifested in a specific query")
title = st.text_input('Twitter query', 'from:twitter')
maxTweets = st.slider('Number of tweets', 10, 250)
if st.button('Submit'):    
    df = scraper(title, maxTweets-1)
    st.write(df)
    sentiments = sentimentAnalysis(df)
    st.write(sentiments)
    sentiments['index'] = range(1, len(df) + 1)
    st.write("Sentiment Analysis")
    st.line_chart(data=sentiments, x="index", y="compound", use_container_width=True)
else:
    st.write('Press the button to submit the query')


