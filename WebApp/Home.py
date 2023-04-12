import streamlit as st
import pandas as pd


st.title("Sentiment Analysis of Text")


st.subheader("Functionalities:")
st.markdown("- **Sentiment Analysis of a group of amazon reviews**")
st.markdown('You can see some stats from the sentiment analysis in a group of amazon reviews and how they correlate with the number of stars given to the product')
st.markdown('For that, visit : <a href="https://miguelamm42-sentimentanalysis-webapphome-riz5x5.streamlit.app/Reviews" target="_self">Reviews</a>', unsafe_allow_html=True)
st.markdown("- **Sentiment Analysis of a group of tweets**")
st.markdown('You can see some stats from a group of tweets, being the main stats the sentiment analysis of the tweets')
st.markdown('An example with the sentiment analysis of tweets about AI and ChatGPT in different weeks can be seen in : <a href="https://miguelamm42-sentimentanalysis-webapphome-riz5x5.streamlit.app/AI" target="_self">AI</a>', unsafe_allow_html=True)
st.markdown('However, the **main functionality of** this web app is the Sentiment Analysis of a group of tweets, obtained from a query. For that, visit : <a href="https://miguelamm42-sentimentanalysis-webapphome-riz5x5.streamlit.app/Query" target="_self">Tweets</a>', unsafe_allow_html=True)

st.subheader("Made by:")
st.markdown("[Inês Vicente](https://github.com/inesvicente2001)")
st.markdown("[Jorge Melo](https://github.com/BatataDoc3)")
st.markdown("[Miguel Martins](https://github.com/MiguelAMM42)")



