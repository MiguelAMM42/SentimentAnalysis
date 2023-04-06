from nltk.sentiment import SentimentIntensityAnalyzer
#nltk.download('vader_lexicon') # only need to run this once
sia = SentimentIntensityAnalyzer()
from utils import loadData, storeData,languages
from tqdm import tqdm
import pandas as pd

def sentimentAnalysis(df):
    res = {}
    for i, row in tqdm(df.iterrows(), total=df.shape[0]):
        text = row['review_text']
        id = row['review_id']
        res[id] = sia.polarity_scores(text)

    sentiments = pd.DataFrame(res).T
    sentiments = sentiments.reset_index().rename(columns={'index': 'review_id'})
    sentiments = sentiments.merge(df, how='left')

    return sentiments


def main():
    for language in languages:
        df = loadData(f"processedData/processed_amazon_reviews_multi_{language.upper()}.csv")
        sentiments = sentimentAnalysis(df)
        storeData(f"analysedData/analysed_amazon_reviews_multi_{language.upper()}.csv",sentiments)

if __name__ == "__main__":
    main()

