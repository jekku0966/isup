import requests
from slacker import Slacker

slack = Slacker('xoxp-3478131362-3477154371-3505081635-51a8a0')
username = 'upbot'
icon_emoji = ':mag:'
keyword = '!up'
text = ''



def post_message(text):
	slack.chat.post_message(text = text,	username = username, icon_emoji = icon_emoji)


if keyword == '!up':
	search = text[4:]
	out = 'http://www.'+search
	outs = 'https://www.'+search
	conn = requests.get(out)
	conn1 = requests.get(outs)
	status = conn.status_code
	status1 = conn1.status_code

	if status == 200 or status1 == 200:
		post_message(search + ' is up. It\'s just you.')
		#print search + ' is up. It\'s just you.'
	else:
		post_message(search + ' is down. Check back later.')
		#print search + ' is down. Check back later.'