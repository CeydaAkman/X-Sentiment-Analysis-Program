import tweepy
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
from dotenv import load_dotenv
import os

load_dotenv()
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def get_tweets(query, count=100):
    tweet_list = []
    for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=count, tweet_fields=["text"]).flatten(limit=count):
        tweet_list.append(tweet.text)
    return tweet_list

def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

hashtag = "#AI"
tweets = get_tweets(hashtag, 100)
df = pd.DataFrame(tweets, columns=["Tweet"])
df['Sentiment'] = df['Tweet'].apply(analyze_sentiment)
sentiment_counts = df['Sentiment'].value_counts().astype(int)
sentiment_colors = {"Positive": "green", "Neutral": "gray", "Negative": "red"}
fig, ax = plt.subplots(figsize=(12, 10))
bars = ax.bar(sentiment_counts.index, sentiment_counts, color=[sentiment_colors[sentiment] for sentiment in sentiment_counts.index])
ax.bar_label(bars, labels=[str(v) for v in sentiment_counts], color='black')

ax.set_title(f'Sentiment Analysis for {hashtag}')
ax.set_xlabel('Sentiment')
ax.set_ylabel('Tweet Count')
plt.show()