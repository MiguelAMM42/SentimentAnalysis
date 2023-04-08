import re
import snscrape.modules.twitter as sntwitter
import pandas as pd
from tqdm import tqdm


def scraper(query, maxTweets):
    scraper = sntwitter.TwitterSearchScraper(query)
    data = scraper.get_items()

    tweets = []

    counter = 0

    for tweet in tqdm(data, total=maxTweets):
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




