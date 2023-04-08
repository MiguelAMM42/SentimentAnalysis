import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
import re
import snscrape.modules.twitter as sntwitter



def scraper(query, maxTweets):
    scraper = sntwitter.TwitterSearchScraper(query)
    data = scraper.get_items()

    tweets = []

    counter = 0

    for tweet in data:
        if counter >= maxTweets:
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


st.title("Twitter Sentiment Analysis")
st.write("A statistical analysis of the sentiments manifested in a group of tweets")
st.write("By default, the tweets are indexed from the most recent to the oldest.")
st.write("However, you can change the order of the tweets to be indexed from the one with the most interations to the one with less.")
title = st.text_input('Twitter query', 'from:twitter')
maxTweets = st.slider('Number of tweets', 10, 250)
option = st.selectbox('Ordering',('Date', 'Interactions'))  
if st.button('Submit'):  
    df = scraper(title, maxTweets)
    if option == 'Interactions':
        df['totalEngagement'] = df['likeCount'] + df['retweetCount'] + df['replyCount']
        df = df.sort_values(by='totalEngagement', ascending=False)
    sentiments = sentimentAnalysis(df)
    sentiments['index'] = range(1, len(df) + 1)
    st.line_chart(data=sentiments, x="index", y="compound", use_container_width=True)
    if option == 'Interactions':
        st.header("Top 5 tweets by engagement")
        st.divider()
    else:
        st.header("5 most recent tweets")
        st.divider()
    for i in range(5):
        date = sentiments.iloc[i]['date'].strftime("%Y/%m/%d %H:%M:%S")
        st.markdown(f"***Tweet Date:*** `{date}`")
        st.markdown(f"***Tweet Content:*** `{sentiments.iloc[i]['renderedContent']}`")
        st.markdown(f"***Tweet Likes:*** `{sentiments.iloc[i]['likeCount']}`")
        st.markdown(f"***Tweet Retweets:*** `{sentiments.iloc[i]['retweetCount']}`")
        st.markdown(f"***Tweet Replies:*** `{sentiments.iloc[i]['replyCount']}`")
        st.markdown(f"***Tweet Hashtags:*** `{sentiments.iloc[i]['hashtags']}`")
        st.markdown(f"***Tweet Sentiment (compound):*** `{sentiments.iloc[i]['compound']}`")
        st.markdown(f"***Tweet Sentiment (positive):*** `{sentiments.iloc[i]['pos']}`")
        st.markdown(f"***Tweet Sentiment (negative):*** `{sentiments.iloc[i]['neg']}`")
        st.markdown(f"***Tweet Sentiment (neutral):*** `{sentiments.iloc[i]['neu']}`")
        st.divider()
else:
    st.write('Press the button to submit the query')


