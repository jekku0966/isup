import requests
from slacker import Slacker

slack = Slacker('xoxp-3478131362-3477154371-3505081635-51a8a0')
username = 'upbot'
icon_emoji = ':mag:'
commands = ['up']



def post_message(text):
	slack.chat.post_message(text = text,	username = username, icon_emoji = icon_emoji)


def respond(text):
	search = text
	out = 'http://www.'+search
	outs = 'https://www.'+search
	conn = requests.get(out)
	conn1 = requests.get(outs)
	status = conn.status_code
	status1 = conn1.status_code

	if status == 200 and status1 == 200:
		post_message(search + ' is up. It\'s just you.')
		#print search + ' is up. It\'s just you.'
	else:
		post_message(search + ' is down. Check back later.')
		#print search + ' is down. Check back later.'


def main():
	text = request.form.get("text", "")

	match = re.findall(r"!(\S+)", text)
	if not match:
		return

		command = match[0]
  	args = text.replace("!%s" % command, '')
  	command = command.lower()

  	if command == '!up':
  		respond()

    	return json.dumps({ })	