#!/usr/bin/python
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT_NUMBER = 9000

# Custom handler for HTTP requests
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
        if self.path == '/':
            # opening home page
            home_template_file = open('C:\\Users\maya.mishra\\Desktop\\Http server\\python-http-server\\home.html').read()
            self.wfile.write(bytes(home_template_file, 'utf-8'))
        elif self.path == '/form/':
            # opening form
            form_template_file = open('C:\\Users\maya.mishra\\Desktop\\Http server\\python-http-server\\form.html').read()
            self.wfile.write(bytes(form_template_file, 'utf-8'))

    def do_HEAD(self):
        self._set_headers()

    # def do_POST(self):
    #     # Doesn't do anything with posted data
    #     self._set_headers()
    #     # file_to_open = open('C:\\Users\maya.mishra\\Desktop\\Http server\\python-http-server\\form.html').read()
    #     # self.wfile.write(self._html("POST!"))
    #     self.wfile.write()

# Create a web server and define the handler to manage the
server = HTTPServer(('', PORT_NUMBER), CustomRequestHandler)
print('Started httpserver on port ' , PORT_NUMBER)

# Wait forever for incoming htto requests
server.serve_forever()
