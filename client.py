import socket
import sys


s = socket.socket()
host = "192.168.43.120"
port = 9999
s.connect((host,port))
while True:
    msg = input()
    if(len(msg)==0):
        break
    s.send(msg.encode())
print("End")
