import twitter
import time
import sys
from OAuthSettings import settings

def get_direct() :
	if 'api' not in globals():
		connect()	
	
	id = get_last_id()

	try:
		messages = api.GetDirectMessages(since_id=id)
	except twitter.TwitterError:
		print 'error getting direct messages'
		return 'Error'

	if messages :        
		id = messages[0].id
		set_last_id(id)	

	return messages

def send_direct(text, user) :
	if 'api' not in globals():
		connect()

        try:
                api.PostDirectMessage(text, screen_name=user)
        except twitter.TwitterError:
                print 'error sending direct message'

def get_last_id() :
	#reads last twitter message id
	f = open( 'last_msg_id.txt', 'r')
	id = f.read()
	f.close()
	return id

def set_last_id(id) :
	#prepares file to write message id
	f = open( 'last_msg_id.txt', 'w')
	f.truncate()
	f.write(str(id))
	f.close()

def connect() :
	global api
	api = twitter.Api(
	consumer_key = settings['consumer_key'],
	consumer_secret = settings['consumer_secret'],
	access_token_key = settings['access_token_key'],
	access_token_secret = settings['access_token_secret'])
