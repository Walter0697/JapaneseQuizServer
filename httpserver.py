# -*- coding: utf-8 -*-
#IMPORT LIBRARY FOR HOSTING SERVER
import time
import BaseHTTPServer
#IMPORT URLLIB TO PARSE DATA
import urllib
#IMPORT TO GET THE DATA
import japanese_converter

#SET UP CONSTANT FOR SERVER
HOST_NAME = "waltercheng.com"
PORT_NUMBER = 9000

#TEMP VARIABLE FOR CONVERTER
database = japanese_converter.JapConverter()

#PARSE THE PATH INTO AN ARRAY
def parsePath(path):
    output = path.split("/")
    return output[1:]

#HANDLER FOR THE SERVER
class ServerHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        currentPath = urllib.unquote(self.path).decode('utf8')
        print "current path: ", currentPath
    
        self.wfile.write(database.getResult(parsePath(currentPath)))

#MAIN FUNCTION
if __name__ == '__main__':
    database.init()
    
    #SET UP THE SERVER
    serverHandle = BaseHTTPServer.HTTPServer
    httpd = serverHandle((HOST_NAME, PORT_NUMBER), ServerHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    database.disconnect()
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)

