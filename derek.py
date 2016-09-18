import sys
import wolfram_api

def ask(text, user) :
	snts = get_sentences(text)

	response = []
	for snt in snts :
		response.append(command(snt))
	return response	

def command(sent) :
	words = get_words(sent)
	return ask_wolfram(sent)

def ask_wolfram(text) :
	return wolfram_api.query(text)

def insert_record(user, text) :
	print user
	print text

#helpers
def get_sentences(text) :
	return filter(bool, text.replace(".", ".\n").replace("?", "?\n").replace("!", "!\n").split('\n'))

def get_words(sentence) :
	return  sentence.replace(',', '').split()

