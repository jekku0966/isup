import requests, json
from slacker import Slacker

slack = Slacker('xoxp-3478131362-3477154371-3505081635-51a8a0')
username = 'upbot'
icon_emoji = 'mag'
commands = ['up']


def post_message(text):
	slack.chat.post_message(text = text,
													username = username,
													icon_emoji = icon_emoji)

def need_help():
	post_message('I look up given address and tell you if it\'s up or naw.')

def respond():
	search = text - command
	out = 'http://www.'+search
	conn = requests.get(out)
	status = conn.status_code

	if  status == 200:
		slack.chat.post_message(search + ' is up. It\'s just you.')
	else:
		slack.chat.post_message(search + 'is down. Check back later.')

def main():
	text = request.form.get("text", "")
	match = re.findall(r"!(\S+)", text)

	if not match:
		return

		command = match[0]
   	args = text.replace("!%s" % command, '')
   	command = command.lower()
   
	if command not in commands:
		post_message('Not sure what "%s" is.' % command)
		return json.dumps({ })

	if command == 'up':
		respond()
	if command == 'up' and 'help':
		need_help()

	return json.dumps({ })
