from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
sia = SentimentIntensityAnalyzer()
from utils import loadData, storeData,languages
from tqdm import tqdm
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def sentimentAnalysis(df):
    res = {}
    for i, row in tqdm(df.iterrows(), total=df.shape[0]):
        text = row['renderedContent']
        id = row['id']
        res[id] = sia.polarity_scores(text)

    sentiments = pd.DataFrame(res).T
    sentiments = sentiments.reset_index().rename(columns={'index': 'id'})
    sentiments = sentiments.merge(df, how='left')

    return sentiments

def process_data():
    df = loadData("Twitter_ChatGPT_AI/scrapped_data.csv")
    sentiments = sentimentAnalysis(df)
    storeData("Twitter_ChatGPT_AI/processed_data.csv", sentiments)
    return sentiments


def make_plot(sentiments):
    a=[]
    pos = 0
    neg = 0
    neu = 0
    nr = 0
    for index, row in sentiments.iterrows():
        pos += row['pos']
        neg += row['neg']
        neu += row['neu']
        nr = index

    a.append(neg/nr)
    a.append(neu/nr)
    a.append(pos/nr)

    print(a)
    left_coordinates=[1,2,3]
    heights=[a[0], a[1], a[2]]
    bar_labels=['Negative','Neutral','Positive']
    plt.bar(left_coordinates,heights,tick_label=bar_labels,width=0.6,color=['red','black'])
    plt.xlabel('Sentiment')
    plt.ylabel('Average')
    plt.title("Sentiment")
    plt.show()


sentiments = process_data()
make_plot(sentiments)

