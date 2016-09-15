import twitter
import maketweet
from OAuthSettings import settings

tweet = maketweet.tweet()
print tweet

consumer_key = settings['consumer_key']
consumer_secret = settings['consumer_secret']
access_token_key = settings['access_token_key']
access_token_secret = settings['access_token_secret']

try:
	api = twitter.Api(
	consumer_key = consumer_key,
	consumer_secret = consumer_secret,
	access_token_key = access_token_key,
	access_token_secret = access_token_secret)

	status = api.PostUpdate(tweet)
	print '  post successful!'

except twitter.TwitterError:
	print 'error posting!'
