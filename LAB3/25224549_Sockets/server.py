1  #!usr/bin/env python3
2
3  import socket
4
5  HOST = '127.0.0.1' #Standard loopback interface address (localhost)
6  PORT = 9999       # Port to listen on
7
8  with socket.socket(socket.AF_INET, socket.SOCKET_STREAM) as s:
9      s.bind((HOST, PORT))
10     s.listen()
11     conn, addr = s.accept()
12     with conn:
13         print('Server is connected with address', addr)
14         while True:
15             data = conn.recv(2048) #default byte stream size
16             if not data:
17                 break
18             conn.sendall(data)
