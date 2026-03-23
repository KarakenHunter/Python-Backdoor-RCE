# Python Reverse Shell (Client-Server)

A simple client-server based reverse shell built using Python.  
This project demonstrates remote command execution, socket communication, and basic fault-tolerant reconnection handling.

---

##  Features

- Persistent client-server connection
- Remote command execution
- Automatic reconnection on connection loss
- Handles both stdout and stderr output
- Delimiter-based communication to prevent incomplete responses
- Lightweight and minimal implementation

---

##  Technologies Used

- Python
- Socket Programming
- Subprocess Module

---

## How It Works

- The **client** connects to the server.
- The **server** sends system commands.
- The client executes the command using the system shell.
- The output is sent back to the server.
- If the connection drops, the client automatically retries.

---

##  Usage

### 1. Start the Server

```bash
python server.py
2. Run the Client
python client.py
3. Execute Commands

Once connected, you can run commands like:

whoami
pwd
dir   # Windows
ls    # Linux
 Project Structure
reverse-shell/
│
├── server.py
├── client.py
└── README.md
 Example Interaction
[+] Listening on port 4444...
[+] Connection from ('127.0.0.1', 52314)

Shell> whoami
user

Shell> pwd
/home/user
 Disclaimer

This project is created for educational purposes only.

Do NOT use this tool on systems without proper authorization. Unauthorized access to systems is illegal and unethical.