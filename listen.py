import twitter
import time
import sys
import tungsten
from OAuthSettings import settings

consumer_key = settings['consumer_key']
consumer_secret = settings['consumer_secret']
access_token_key = settings['access_token_key']
access_token_secret = settings['access_token_secret']
wolfram_key = settings['wolfram_key']

num_arg = len(sys.argv)
if (num_arg > 1) :
	num = int(sys.argv[1])
	if (num_arg > 2) :
		sleep = int(sys.argv[2])
		if (num_arg > 3) :
			print 'Too many arguments'
	else:
		sleep = 10
else:
	num = 1
	sleep = 10

f = open( 'last_msg_id.txt', 'r')
id = f.read()
f.close()
f = open( 'last_msg_id.txt', 'w')

client = tungsten.Tungsten(wolfram_key)
print client
result = client.query('pi')
print result
print len(result.pods)
print result.error

for pod in result.pods:
	print 'here'
	print pod.title

count = 0
while (count < num) :
	try:
		api = twitter.Api(
		consumer_key = consumer_key,
		consumer_secret = consumer_secret,
		access_token_key = access_token_key,
		access_token_secret = access_token_secret)
	
		messages = api.GetDirectMessages(since_id=id)

		update = True
		for msg in messages:
   			print msg.text
			print msg.id
			if (update) :
				id = msg.id
				update = False;
			api.PostDirectMessage(msg.text, screen_name=msg.sender_screen_name)
			
			result = client.query(msg.text)
			for pod in result.pods:
        			print 'here'
        			print pod.title			
				api.PostDirectMessage(pd.title, screen_name='milmd90')

	except twitter.TwitterError:
		print 'error listening!'

	count = count + 1
	if (count < num) :
		time.sleep(sleep)

f.truncate()
f.write(str(id))
f.close()


