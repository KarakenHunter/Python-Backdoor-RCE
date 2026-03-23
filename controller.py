import socket

host='localhost'
port=9821
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen()
print("[*]Waiting for connection...")

