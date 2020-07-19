# Twitter Web Services


import tweepy, os


consumer_key = os.environ['twitter_consumer_key']
consumer_secret	= os.environ['twitter_consumer_secret']
access_token	= os.environ['twitter_access_token']
access_secret	= os.environ['twitter_access_secret']


auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


tweets = api.search(q='#python')


# display results to screen
for t in tweets:
	print(t.created_at, t.text, '\n')