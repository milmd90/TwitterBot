from pymongo import MongoClient

def insert(id, user, text) :
	con = MongoClient()
	coll = con['TwitterBot']['msg']
	coll.insert_one({'msg_id':id, 'user':user, 'text':text})
	print 'Insert ' + text
	return 'Inserted record'

def find(user) :
	print 'Find ' + user
	con = MongoClient()
	coll = con['TwitterBot']['msg']
	cursor = coll.find({'user': user})
	msgs = ''
	for doc in cursor:
		print doc
		msgs += (doc['text'] + '\n')
	return msgs
