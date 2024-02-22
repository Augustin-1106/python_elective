import socket
import threading

HEADER = 64
PORT = 6000
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def receive():
    while True:
        in_msg = client.recv(1024).decode(FORMAT)
        print(in_msg)
        if in_msg == DISCONNECT_MESSAGE:
            break

def write():
    while True:
        string = input("Sender message:")
        send(string)
        if string == DISCONNECT_MESSAGE:
            break

receiver = threading.Thread(target=receive)
receiver.start()
sender = threading.Thread(target=write)
sender.start()