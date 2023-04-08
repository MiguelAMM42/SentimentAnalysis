from src.scraper import scraper
from src.sentimentAnalysis import processData
from src.utils import storeData


def main():
    query = "#chatgpt OR #AI min_replies:10 min_faves:100 min_retweets:100"
    df = scraper(query, 1000)
    storeData("data/chatGPT_AI/scrappedData.csv", df)
    sentiments = processData(df)
    storeData("data/chatGPT_AI/processedData.csv", sentiments)



if __name__ == "__main__":
    main()