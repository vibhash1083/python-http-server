#!/usr/bin/python
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT_NUMBER = 9000

#This class will handles any incoming request from
#the browser 
class CustomRequestHandler(BaseHTTPRequestHandler):
	
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _html(self, message):
        """This just generates an HTML document that includes `message`
        in the body. Override, or re-write this do do more interesting stuff.

        """
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")  # NOTE: must return a bytes object!

    def do_GET(self):
        self._set_headers()
        self.wfile.write(self._html("hi!"))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write(self._html("POST!"))

#Create a web server and define the handler to manage the
#incoming request
server = HTTPServer(('', PORT_NUMBER), CustomRequestHandler)
print('Started httpserver on port ' , PORT_NUMBER)

#Wait forever for incoming htto requests
server.serve_forever()
