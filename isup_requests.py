import requests

keyword = raw_input('Enter keyword(ie. !up or !ups) : ')

if keyword == '!up':

	test = raw_input('Enter url (ie. reddit.com): ')
	out = 'http://www.'+test
	conn = requests.get(out)
	r1 = conn.status_code

	if r1 == 200:
		print out + " is up. It's just you."
	else:
		print out + " is down. Check back later"

elif keyword == '!ups':

	test = raw_input('Enter url (ie. reddit.com): ')
	out = 'http://www.'+test
	conn = requests.get(out)
	r1 = conn.status_code

	if r1 == 200:
		print out + " is up. It's just you."
	else:
		print out + " is down. Check back later"