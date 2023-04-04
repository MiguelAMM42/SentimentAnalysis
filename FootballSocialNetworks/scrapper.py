import pandas as pd
from tqdm.notebook import tqdm
import snscrape.modules.twitter as sntwitter
import snscrape.modules.instagram as sninstagram
import json

# Paulinho idea is no more :(
"""
scraper = sntwitter.TwitterSearchScraper('Paulinho')

tweets = []
for i, tweet in enumerate(scraper.get_items()):
    if i > 10:
        break
    tweets.append(tweet)


df = pd.DataFrame(tweets)
print(df)

for tweet in tweets:
    print(tweet.rawContent)
"""

with open('socialNetworks.json', 'r') as f:
    socialNetworks = json.load(f)


dataComplete = pd.DataFrame()

for socialNet in socialNetworks:
    print(socialNet)
    # para instagram o scrapper não funciona...
    """
    instagram = socialNet['instagram']
    scraper = sninstagram.InstagramUserScraper(instagram)
    user = scraper._get_entity()
    print(user)
    """
    twitter_account = socialNet['twitter']
    """ Will be useful if I want to get stats from tweets by the user """
    #data = scraper.get_items()
    #for i,content in enumerate(data):
        #print(content)
        #if i > 10:
            #break
    # Search query
    query = f"from:{twitter_account}"

    scraper = sntwitter.TwitterSearchScraper(query)
    data = scraper.get_items()

    # Use snscrape to get tweets from the account
    tweets = []

    for i, tweet in enumerate(data):
        if i > 2:
            break
        print(f"{i}: {tweet.rawContent}")
        tweets.append(tweet)


    # Get the number of followers from the first tweet (the account info tweet)
    num_followers = tweets[0].user.followersCount

    print(f"{twitter_account} has {num_followers} followers.")
    
    



# https://www.youtube.com/watch?v=PUMMCLrVn8A

# https://github.com/JustAnotherArchivist/snscrape

# https://streamlit.io/

# https://github.com/lfcc1/spln2223/blob/main/TP1/Modulos.md
