import tweepy
from textblob import TextBlob

consumer_key='your api'
consumer_secret='your secret key'
access_token_key='your token key'
access_token_secret='your token'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token_key,access_token_secret)
 
api = tweepy.API(auth)

pbtweet = api.search('#happy')

for tweet in pbtweet:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)


# this example will help us to know abt peple tweeting in twetter are the happy or angry "
# if it Sentiment(polarity=-1 [angry],polarity=-1 [happy]