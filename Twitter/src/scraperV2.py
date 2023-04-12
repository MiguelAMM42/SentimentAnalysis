import pandas as pd
import re
from tqdm import tqdm
import snscrape.modules.twitter as sntwitter


def scraperV2(_query_, maxTweets, weeks) :

    tweets = []
    
    for week in weeks:
        query = _query_ + f" since:{week['byear']}-{week['bmonth']}-{week['bday']} until:{week['eyear']}-{week['emonth']}-{week['eday']}"

        scraper = sntwitter.TwitterSearchScraper(query)
        data = scraper.get_items()

        counter = 0
        weekCSV = f"{week['byear']}/{week['bmonth']}/{week['bday']}-{week['eyear']}/{week['emonth']}/{week['eday']}"

        for tweet in tqdm(data, total=maxTweets):
            if counter > maxTweets:
                break
                    
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
            l.append(weekCSV)
            tweets.append(l)
            counter +=1

    df = pd.DataFrame(tweets, columns = ['id', 'date', 'renderedContent', 'likeCount', 'retweetCount', 'replyCount','hashtags','week'])

    return df

