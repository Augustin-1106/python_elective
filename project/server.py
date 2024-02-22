import socket
import threading

HEADER = 64
FORMAT = 'utf-8'
PORT = 6000
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"
CONNECT_MESSAGE = "!CONNECT"
CLIENT_LIST = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def receive(conn):
    msg_length = conn.recv(HEADER).decode(FORMAT)
    if  msg_length:
        msg_length = int(msg_length)
        return conn.recv(msg_length).decode(FORMAT)
    
def post(connectionList, msg):
    for conn in connectionList:
        conn.send(msg.encode(FORMAT))


def client_handler(conn, addr):
    connectionList = []
    #connectionList.append(conn)
    print(f"New Connection {addr} added")

    while True:
        # Receive message
        msg = receive(conn)

        #Conditions
        if DISCONNECT_MESSAGE in msg:
            address = msg.split(":")
            if len(address) == 1:
                print(f"[{addr}] : DISCONNECTED")
                conn.send("!DISCONNECT".encode(FORMAT))
                break
            elif len(address) == 2:

                connectionList.remove(CLIENT_LIST[int(address[1])])
                print(f"[{addr}] : DISCONNECTED from [{msg}]")

        elif CONNECT_MESSAGE in msg:
            address = int(msg.split(":")[1])
            connectionList.append(CLIENT_LIST[address])
            print(f"[{addr}] : CONNECTED to [{address}]")

        print(f"[{addr}] : {msg}") #Display message in terminal

        #Send message
        post(connectionList, msg)

    conn.close()
        
    

def initiate():
    server.listen()
    print(f"Server is Listening on {SERVER}")
    while True:
        conn,addr = server.accept()

        CLIENT_LIST[addr[1]] = conn
        print(f"Connection is established at {addr}")

        thread = threading.Thread(target=client_handler, args=(conn,addr))
        thread.start()
        print(f"Number of connections = {threading.active_count()-1}")

print("Initiating SERVER..")
initiate()