import tungsten
from OAuthSettings import settings

def query(msg) :
	#initalize tungsten to query wolfram
	wolfram_key = settings['wolfram_key']
	client = tungsten.Tungsten(wolfram_key)
	result = client.query(msg)

	response = ''
	for pod in result.pods:
		response += (pod.title) + ':\n'
		sections = pod.format['plaintext']
		for section in sections:
			if section is not None:
				response += (section + '\n')
				response += '\n'
	return response
