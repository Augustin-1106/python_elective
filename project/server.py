import socket
import threading

HEADER = 64
FORMAT = 'utf-8'
PORT = 6000
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"
CONNECT_MESSAGE = "!CONNECT"
ID_MESSAGE = "!ID"
CLIENT_LIST = {}
CLIENT_ID = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def receive(conn):
    msg_length = conn.recv(HEADER).decode(FORMAT)
    if  msg_length:
        msg_length = int(msg_length)
        return conn.recv(msg_length).decode(FORMAT)
    
def post(connectionList, msg):
    for id in connectionList:
        try:
            CLIENT_LIST[id].send(msg.encode(FORMAT))
        except:
            continue


def client_handler(conn, addr):
    connectionList = []
    #connectionList.append(conn)
    print(f"New Connection {addr} added")

    while True:
        # Receive message
        msg = receive(conn)

        #Conditions
        if DISCONNECT_MESSAGE in msg:
            id = msg.split(":")
            if len(id) == 1:
                print(f"[{addr}] : DISCONNECTED")
                conn.send("!DISCONNECT".encode(FORMAT))
                break
            elif len(id) == 2:

                connectionList.remove(id[1])
                print(f"[{addr}] : DISCONNECTED from [{msg}]")

        elif CONNECT_MESSAGE in msg:
            id = msg.split(":")[1]
            connectionList.append(id)
            print(f"[{addr}] : CONNECTED to [{id}]")

        elif ID_MESSAGE in msg:
            id = msg.split(":")[1]
            CLIENT_LIST[id] = conn
            print(CLIENT_LIST)

        print(f"[{addr}] : {msg}") #Display message in terminal

        #Send message
        post(connectionList, msg)

    conn.close()
        
    

def initiate():
    server.listen()
    print(f"Server is Listening on {SERVER}")
    while True:
        conn,addr = server.accept()

        #CLIENT_LIST[addr[1]] = conn
        print(f"Connection is established at {addr}")

        thread = threading.Thread(target=client_handler, args=(conn,addr))
        thread.start()
        print(f"Number of connections = {threading.active_count()-1}")

print("Initiating SERVER..")
initiate()