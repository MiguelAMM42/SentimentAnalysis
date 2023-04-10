import pandas as pd
import csv
import re
from tqdm.notebook import tqdm
import snscrape.modules.twitter as sntwitter
import snscrape.modules.instagram as sninstagram


query1 = "(#chatgpt OR #AI) lang:en"

def twitter_chatgpt_ai(query) :

    scraper = sntwitter.TwitterSearchScraper(query)
    data = scraper.get_items()

    tweets = []

    f = open('Twitter_ChatGPT_AI/scrapped_data.csv', 'w', encoding='UTF8')
    writer = csv.writer(f)

    header = ['id', 'date', 'renderedContent', 'likeCount', 'retweetCount', 'replyCount', 'inReplyToTweetId', 'hashtags']

    writer.writerow(header)
    counter = 0

    for tweet in data:
        if counter > 2000:
            break

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
        l.append(tweet.replyCount)
        l.append(tweet.inReplyToTweetId)
        l.append(tweet.hashtags)
        writer.writerow(l)
        #print(f"{counter}")
        counter +=1

    f.close()


weeks = [
    {'byear': '2023', 'bmonth': '04', 'bday': '02', 'eyear': '2023', 'emonth': '04', 'eday': '09'},
    {'byear': '2023', 'bmonth': '03', 'bday': '26', 'eyear': '2023', 'emonth': '04', 'eday': '01'},
    {'byear': '2023', 'bmonth': '03', 'bday': '19', 'eyear': '2023', 'emonth': '03', 'eday': '25'},
    {'byear': '2023', 'bmonth': '03', 'bday': '12', 'eyear': '2023', 'emonth': '03', 'eday': '18'},
    {'byear': '2023', 'bmonth': '03', 'bday': '05', 'eyear': '2023', 'emonth': '03', 'eday': '11'},
    {'byear': '2023', 'bmonth': '02', 'bday': '26', 'eyear': '2023', 'emonth': '03', 'eday': '04'},
    {'byear': '2023', 'bmonth': '02', 'bday': '19', 'eyear': '2023', 'emonth': '02', 'eday': '25'},
    {'byear': '2023', 'bmonth': '02', 'bday': '12', 'eyear': '2023', 'emonth': '02', 'eday': '18'},
    {'byear': '2023', 'bmonth': '02', 'bday': '05', 'eyear': '2023', 'emonth': '02', 'eday': '11'},
    {'byear': '2023', 'bmonth': '01', 'bday': '29', 'eyear': '2023', 'emonth': '02', 'eday': '04'},
    {'byear': '2023', 'bmonth': '01', 'bday': '22', 'eyear': '2023', 'emonth': '01', 'eday': '28'},
    {'byear': '2023', 'bmonth': '01', 'bday': '15', 'eyear': '2023', 'emonth': '01', 'eday': '21'},
    {'byear': '2023', 'bmonth': '01', 'bday': '08', 'eyear': '2023', 'emonth': '01', 'eday': '14'},
    {'byear': '2023', 'bmonth': '01', 'bday': '01', 'eyear': '2023', 'emonth': '01', 'eday': '07'},
    {'byear': '2022', 'bmonth': '12', 'bday': '25', 'eyear': '2022', 'emonth': '12', 'eday': '31'},
    {'byear': '2022', 'bmonth': '12', 'bday': '18', 'eyear': '2022', 'emonth': '12', 'eday': '24'},
    {'byear': '2022', 'bmonth': '12', 'bday': '11', 'eyear': '2022', 'emonth': '12', 'eday': '17'},
    {'byear': '2022', 'bmonth': '12', 'bday': '04', 'eyear': '2022', 'emonth': '12', 'eday': '10'},
    {'byear': '2022', 'bmonth': '11', 'bday': '27', 'eyear': '2022', 'emonth': '12', 'eday': '03'},
    {'byear': '2022', 'bmonth': '11', 'bday': '20', 'eyear': '2022', 'emonth': '11', 'eday': '26'},
    {'byear': '2022', 'bmonth': '11', 'bday': '13', 'eyear': '2022', 'emonth': '11', 'eday': '19'},
    {'byear': '2022', 'bmonth': '11', 'bday': '06', 'eyear': '2022', 'emonth': '11', 'eday': '12'},
    {'byear': '2022', 'bmonth': '10', 'bday': '30', 'eyear': '2022', 'emonth': '11', 'eday': '05'},
    {'byear': '2022', 'bmonth': '10', 'bday': '23', 'eyear': '2022', 'emonth': '10', 'eday': '29'},
]


def twitter_chatgpt_ai_by_date() :

    f = open('scrapped_data_date.csv', 'w', encoding='UTF8')
    writer = csv.writer(f)

    header = ['id', 'date', 'renderedContent', 'likeCount', 'retweetCount', 'replyCount', 'inReplyToTweetId', 'hashtags']
    writer.writerow(header)
    
    for week in weeks:
        query = f"(#chatgpt OR #AI) lang:en since:{week['byear']}-{week['bmonth']}-{week['bday']} until:{week['eyear']}-{week['emonth']}-{week['eday']}"

        scraper = sntwitter.TwitterSearchScraper(query)
        data = scraper.get_items()

        tweets = []

        counter = 0

        for tweet in data:
            if counter > 50:
                break

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
            l.append(tweet.replyCount)
            l.append(tweet.inReplyToTweetId)
            l.append(tweet.hashtags)
            writer.writerow(l)
            #print(f"{counter}")
            counter +=1

    f.close()




#twitter_chatgpt_ai(query)

twitter_chatgpt_ai_by_date()