1  #!/usr/bin/env python3
2
3  import socket
4
5  HOST = '127.0.0.1'  # The server's hostname or IP address 
6  PORT = 9999        # The port used by the server
7
8  with socket.socket(socket.AF_INET, socket.SOCKET_STREAM) as s:
9      s.connect((HOST, PORT))
10     s.sendall(b'Hello',Server
11     data = s.recv(1024)
12
13  print('Received', repr(data))