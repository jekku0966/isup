import cherrypy
import json
import requests

class IsUp(object):
    exposed = True

    # Make cherrypy accept content type
    #@cherrypy.tools.accept(media='*/*')
  
    def POST(self, **kwargs):

       # Uncomment console output
       print cherrypy.request.body.params

       # Parse received json
       json_parse = json.dumps(cherrypy.request.body.params)
       # Decode the json
       decoded = json.loads(json_parse)
       print decoded
       # Transfer decoded json from {"text": "!up <http://google.com|google.com>"} to trigger
       trigger = decoded['text']
       # Select only the first 3 from the trigger
       keyword = trigger[:3]
       # Split !up <http://google.com|google.com> to 2 different with from | and select the latter and remove '>'
       url = trigger.split('|')[1][:-1]

       # Uncomment for console output of keyword and url
       print keyword
       print url

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
        if status == 200 or status1 == 200:
          return json.dumps({'text': '%s is up. It\'s just you.' % url})
        else:
          return json.dumps({'text':'%s is down. Check back later.' % url})

        
if __name__ == '__main__':
    cherrypy.config.update("server.conf")
    cherrypy.quickstart(IsUp(), '/', "app.conf")