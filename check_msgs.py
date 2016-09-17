import sys
import time
import twitter_api
import derek

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

count = 0
while (count < num) :
	messages = twitter_api.get_direct()

	if not isinstance(messages, list) :
		print 'check not list'
		print messages
		sys.exit(1)

	for msg in messages:
		response = derek.ask(msg.text)
		twitter_api.send_direct(response, msg.sender_screen_name)

	count = count + 1
	if (count < num) :
		time.sleep(sleep)
