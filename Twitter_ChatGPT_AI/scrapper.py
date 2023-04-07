import pandas as pd
import csv
import re
from tqdm.notebook import tqdm
import snscrape.modules.twitter as sntwitter
import snscrape.modules.instagram as sninstagram

query = "#chatgpt OR #AI"


def twitter_chatgpt_ai(query) :

    scraper = sntwitter.TwitterSearchScraper(query)
    data = scraper.get_items()

    tweets = []

    f = open('scrapped_data.csv', 'w', encoding='UTF8')
    writer = csv.writer(f)

    header = ['id', 'date', 'renderedContent', 'likeCount', 'retweetCount', 'replyCount', 'inReplyToTweetId', 'hashtags']

    writer.writerow(header)

    for i, tweet in enumerate(data):
        if i > 20:
            break
        if (tweet.lang == 'en') :
            tweets.append(tweet)
            text = tweet.renderedContent
            text = re.sub(',','\\,',text)
            text = re.sub('\n',' ',text)
            l = []
            l.append(tweet.id)
            l.append(tweet.date)
            l.append(text)
            l.append(tweet.likeCount)
            l.append(tweet.retweetCount)
            l.append(tweet.inReplyToTweetId)
            l.append(tweet.hashtags)
            writer.writerow(l)
            print(f"{i}: {tweet.rawContent, tweet.vibe}")

    f.close()





twitter_chatgpt_ai(query)