import socket
import threading

HEADER = 64
PORT = 6000
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
REJECT_MESSAGE = "!REJECT"
APPROVE_MESSAGE = "!APPROVE"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

#Send message
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

#receive messsage
def receive():
    while True:
        in_msg = client.recv(1024).decode(FORMAT)
        print(in_msg)
        if in_msg == DISCONNECT_MESSAGE:
            break        

#write message
def write():
    while True:
        message = input("Sender message:")
        send(message)
        if message == DISCONNECT_MESSAGE:
            break

#ID Verification
def send_id():
    id = "!ID:" + input("Enter id:")
    send(id)

    in_msg = client.recv(1024).decode(FORMAT)

    if in_msg == REJECT_MESSAGE:
        print("----CONNECTION WITH SERVER REJECTED----")
        send_id()
    elif in_msg == APPROVE_MESSAGE:
        print("----CONNECTION WITH SERVER ESTABLISHED----")

send_id()

receiver = threading.Thread(target=receive)
receiver.start()
sender = threading.Thread(target=write)
sender.start()