import requests, json

# Local testing area
#keyword = raw_input('Enter keyword(ie. !up or !ups) : ')
search = payload.json("text": "%s")
trigger_word = '!up'

if search == 'help':
	payload = {"text": "I look up given address and tell you if it's up or naw."}
	#print 'I look up given address and tell you if it\'s up or naw.'

if trigger_word == '!up' and search != 'help':

	out = 'http://www.'+search
	conn = requests.get(out)
	status = conn.status_code

	if  status == 200:
		payload = {"text": search + " is up. It's just you."}
		#print search + " is up. It's just you." #For local testing
	else:
		payload = {"text": search + " is up. It's just you."}
		#print search + " is up. It's just you." #For local testing