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
REJECT_MESSAGE = "!REJECT"
APPROVE_MESSAGE = "!APPROVE"
CLIENT_LIST = {}

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
    print(f"New Connection {addr} added")

    while True:
        # Receive message
        msg = receive(conn)

        #Conditions

    #Disconnect Command
        if DISCONNECT_MESSAGE in msg:
            id = msg.split(":")
            if len(id) == 1:
                print(f"[{addr}] : DISCONNECTED")
                conn.send("!DISCONNECT".encode(FORMAT))
                del CLIENT_LIST[my_id]
                break
            elif len(id) == 2:

                connectionList.remove(id[1])
                print(f"[{addr}] : DISCONNECTED from [{msg}]")

    #Connect Command
        elif CONNECT_MESSAGE in msg:
            id = msg.split(":")[1]
            connectionList.append(id)
            print(f"[{addr}] : CONNECTED to [{id}]")

    # Client Verification
        elif ID_MESSAGE in msg:
            id = msg.split(":")[1]
            if id not in CLIENT_LIST:
                my_id = id
                CLIENT_LIST[id] = conn
                conn.send(APPROVE_MESSAGE.encode(FORMAT))
                print(CLIENT_LIST)
                continue
            else:
                conn.send(REJECT_MESSAGE.encode(FORMAT))
                continue

        #End of Conditions

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