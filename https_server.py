# https_server_python
import socketserver
import http.server
import ssl
import os


httpd = socketserver.TCPServer(('localhost', 8000), 
                http.server.SimpleHTTPRequestHandler)

path = '/'
BASE_DIR = os.path.basename(path)
print(BASE_DIR)

httpd.socket = ssl.wrap_socket(httpd.socket,
                certfile=BASE_DIR+"server.pem",
                keyfile=BASE_DIR+"server.key",
                server_side=True)

httpd.serve_forever()