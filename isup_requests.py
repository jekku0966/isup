import requests, json

# Local testing area
#keyword = raw_input('Enter keyword(ie. !up or !ups) : ')
test = 'help'
trigger_word = '!up'

if test == 'help':
	#payload = {"text": "I look up given address and tell you if it's up or naw."}
	print 'I look up given address and tell you if it\'s up or naw.'

if trigger_word == '!up' and test != 'help':

	out = 'http://www.'+test
	conn = requests.get(out)
	status = conn.status_code

	if  status == 200:
		#payload = {"text": out + " is up. It's just you."}
		print test + " is up. It's just you." #For local testing
	else:
		#payload = {"text": test + " is up. It's just you."}
		print test + " is up. It's just you." #For local testing