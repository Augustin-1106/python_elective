import socket
import threading
import queue

HEADER = 64
PORT = 6000
SERVER = socket.gethostbyname('Adam')
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
REJECT_MESSAGE = "!REJECT"
APPROVE_MESSAGE = "!APPROVE"
CONNECT_MESSAGE = "!CONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

#Crete a queue
msg_queue = queue.Queue()

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
        if CONNECT_MESSAGE in in_msg:
            continue
        if APPROVE_MESSAGE in in_msg:
            continue
        print(in_msg)
        msg_queue.put(in_msg)
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
def send_id(id):
    send(id)

    in_msg = client.recv(1024).decode(FORMAT)

    if in_msg == REJECT_MESSAGE:
        print("----CONNECTION WITH SERVER REJECTED----")
        send_id()
    elif in_msg == APPROVE_MESSAGE:
        print("----CONNECTION WITH SERVER ESTABLISHED----")

def main():

    id = "!ID:" + input("Enter id:")
    send_id(id)
    write()

receiver = threading.Thread(target=receive)
receiver.start()
        
if __name__ == "__main__":
    main()