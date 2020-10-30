import tweepy

## Consumer and Aceess key info ##
## Please provide user specific twitter keys for below , in the place of SECRET_KEY ##
CONSUMER_KEY = 'SECRET_KEY'
CONSUMER_SECRET = 'SECRET_KEY'
ACCESS_KEY = 'SECRET_KEY'
ACCESS_SECRET = 'SECRET_KEY'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


trends1 = api.trends_place(1)


hashtags = [x['name'] for x in trends1[0]['trends'] if x['name'].startswith('#')]


## top 10 trending tweets with hastags
for hashtag in hashtags[:10]:
	print(hashtag+"\n")