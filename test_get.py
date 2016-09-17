import sys
import twitter_api

messages = twitter_api.get_direct()
print 'here are your messages'
print messages

if not isinstance(messages, list) :
	print 'messages arent a list'
	print messages
	sys.exit(1)

for msg in messages:
	print msg.id
	print msg.text
