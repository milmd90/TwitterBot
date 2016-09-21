import sys
import wolfram_api
import mongo

def ask(id, user, text) :
	snts = get_sentences(text)

	response = []
	for snt in snts :
		response.append(command(id, user, snt))
	return response	

def command(id, user, sent) :
	words = get_words(sent)
	action = words[0]
	words.pop(0)
	msg = ' '.join(words)
	if action == 'Wolfram' :
		return wolfram_api.query(msg)
	elif action == 'Insert' :
		return mongo.insert(id, user, msg)
	elif action == 'Find' :
		return mongo.find(user)
	else :
		print 'Invlid request'

#helpers
def get_sentences(text) :
	return filter(bool, text.replace(".", ".\n").replace("?", "?\n").replace("!", "!\n").split('\n'))

def get_words(sentence) :
	return  sentence.replace(',', '').split(' ')

