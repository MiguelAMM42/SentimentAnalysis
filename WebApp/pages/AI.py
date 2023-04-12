import streamlit as st
import pandas as pd
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

__path__ = os.path.join(APP_ROOT, "../static/chatGPT_AI/processedData.csv")

st.title("A statistical analysis of the sentiments manifested about AI and ChatGPT")
st.subheader("Analysis done by different weeks")

st.markdown('The tweets were scraped using the following query: `(#chatgpt OR #AI) lang:en min_replies:1 min_faves:10 min_retweets:5 since:YYYY-MM-DD until:YYYY-MM-DD`')

with open(__path__, "r") as fCSV:
    df = pd.read_csv(fCSV)
    df['index'] = range(1, len(df) + 1)


weeks = df['week'].unique().tolist()
option = st.selectbox(
    'What week do you wish to select?',
    weeks)

st.header(f'Sentiment Analysis in Week: {option}')
st.line_chart(df.loc[df['week'] == option], x='index', y='compound', height=500, use_container_width=True)
st.divider()
st.subheader("Example of a tweet in this week")
tweet = df.loc[df['week'] == option].sample(1)
date = tweet['date'].values[0].split('T')[0].split('+')[0]
st.markdown(f"***Tweet Date:*** `{date}`")
st.markdown(f"***Tweet Content:*** `{tweet['renderedContent'].values[0]}`")
st.markdown(f"***Tweet Likes:*** `{tweet['likeCount'].values[0]}`")
st.markdown(f"***Tweet Retweets:*** `{tweet['retweetCount'].values[0]}`")
st.markdown(f"***Tweet Replies:*** `{tweet['replyCount'].values[0]}`")
st.markdown(f"***Tweet Hashtags:*** `{tweet['hashtags'].values[0]}`")
st.markdown(f"***Tweet Sentiment (compound):*** `{tweet['compound'].values[0]}`")
st.markdown(f"***Tweet Sentiment (positive):*** `{tweet['pos'].values[0]}`")
st.markdown(f"***Tweet Sentiment (negative):*** `{tweet['neg'].values[0]}`")
st.markdown(f"***Tweet Sentiment (neutral):*** `{tweet['neu'].values[0]}`")


