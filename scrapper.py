import pandas as pd
from tqdm.notebook import tqdm
import snscrape.modules.twitter as sntwitter

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



# https://www.youtube.com/watch?v=PUMMCLrVn8A

# https://github.com/JustAnotherArchivist/snscrape

# https://streamlit.io/

# https://github.com/lfcc1/spln2223/blob/main/TP1/Modulos.md
