import snscrape.modules.twitter as sntwitter

# Twitter account name
account_name = "Twitter"

# Search query
query = f"from:{account_name}"

scraper = sntwitter.TwitterSearchScraper(query)
data = scraper.get_items()

# Use snscrape to get tweets from the account
tweets = []

for i, tweet in enumerate(data):
    if i > 2:
        break
    #print(f"{i}: {tweet.rawContent}")
    tweets.append(tweet)


# Get the number of followers from the first tweet (the account info tweet)
num_followers = tweets[0].user.followersCount

print(f"{account_name} has {num_followers} followers.")