import requests
from slacker import Slacker

#Slack related
slack = Slacker('xoxp-3478131362-3477154371-3505081635-51a8a0')
#channel = '#developers'
username = 'upbot'
icon_emoji = ':mag:'

#Search related
trigger_word = '!up'
keyword = trigger_word
text = 'facebook.com'


#Defining post format
def post_message(text):
	slack.chat.post_message(channel = None, text = text,	username = username, icon_emoji = icon_emoji)

def response():
	if keyword == '!up':
		search = text
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
