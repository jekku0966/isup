import cherrypy
import json
import requests

class IsUp(object):
    exposed = True
    # Make cherrypy accept json
    @cherrypy.tools.accept(media='application/x-www-form-urlencoded')
    # Make cherrypy understand json
    @cherrypy.tools.json_in()
    

    def POST(self, **kwargs):
       # Uncomment for json console output
       print cherrypy.request.json

       # Parse received json
       json_parse = json.dumps(cherrypy.request.json)
       # Decode the json
       decoded = json.loads(json_parse)
       print decoded
       # Transfer decoded json from {"message":{"text": "!up google.com"}} to trigger
       trigger = decoded['message']['text']
       # Select only the first 3 from the trigger
       keyword = trigger[:3]
       # Split !up <http:\/\/google.com|google.com to 2 different with from | and select the latter and remove '>'
       url = trigger.split('|')[1][:-1]

       # Uncomment for console output of keyword and url
       #print keyword
       #print url

       if keyword == '!up':

           # Morph url as normal HTTP
           out = 'http://www.'+url
           # Morph url as HTTPS
           outs = 'https://www.'+url
           # Check for HTTP signal
           conn = requests.get(out)
           # Check for HTTPS signal
           conn1 = requests.get(outs)
           # Ask the status 200/OK for HTTP
           status = conn.status_code
           # Ask the status 200/OK for HTTPS
           status1 = conn1.status_code
           # Check if the server return 200/OK or not.

           # Wheter the status for HTTP or HTTPS is 200/OK return URL is up otherwise return it's down
           if status == 200 or status1 == 200:
               return url+' is up. It\'s just you.'
           else:
               return url+' is down. Check back later.'
    

        
if __name__ == '__main__':
    cherrypy.config.update("server.conf")
    cherrypy.quickstart(IsUp(), '/', "app.conf")