import socket

host='localhost'
port=9822
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen()
print("[*]Waiting for connection...")

client, addr=sock.accept()
print(f"Connected to {addr}")
while True:
    cmd=input("~$ ")
    if cmd.lower=='quit' or cmd.lower=='exit':
        print("Connection closed successfully!")
        client.close()
        sock.close()
    else:
        client.send(cmd.encode('utf-8'))
        resp=client.recv(4096)
        print(resp.decode('utf-8'))