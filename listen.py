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

#sets up default arguments
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

#reads last twitter message id
f = open( 'last_msg_id.txt', 'r')
id = f.read()
f.close()

#prepares file to write message id
f = open( 'last_msg_id.txt', 'w')

#initalize tungsten to query wolfram
client = tungsten.Tungsten(wolfram_key)

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
			if (update) :
				id = msg.id
				update = False
			
			result = client.query(msg.text)
			
			response = ''
			for pod in result.pods:
				response += (pod.title) + ':\n'
				sections = pod.format['plaintext']
				for section in sections:
					if section is not None:
						response += (section + '\n')
				response += '\n'

			api.PostDirectMessage(response, screen_name=msg.sender_screen_name)

	except twitter.TwitterError:
		print 'error listening!'

	count = count + 1
	if (count < num) :
		time.sleep(sleep)

f.truncate()
f.write(str(id))
f.close()


