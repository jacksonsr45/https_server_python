# https_server_python

---
## creating the keys

cole in your terminal this code 
```
openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout server.key -out server.pem
```

The 2 files must be in the directory indicated.

```py
path = '/'# Here I point the location of the files
BASE_DIR = os.path.basename(path)
print(BASE_DIR)

httpd.socket = ssl.wrap_socket(httpd.socket,
                certfile=BASE_DIR+"server.pem",
                keyfile=BASE_DIR+"server.key",
                server_side=True)
```
