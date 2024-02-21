import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

client_list = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr, client_list):
    print(f"[NEW CONNECTION] {addr} connected")
    list =False

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if  msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            print(msg)
            if "!CONNECT" in msg:
                address = int(msg.split(':')[1])
                list = True
                print(type(address))
            if msg == DISCONNECT_MESSAGE:
                connected = False
                conn.send("!DISCONNECT ".encode(FORMAT))
            
            print(f"[{addr}]: {msg}")
            conn.send("Msg sent ".encode(FORMAT))
            try:
                if list:
                    if address in client_list:
                        print(client_list[address])
                        print("**************************************************************")
                        client_list[address].send(msg.encode(FORMAT))
            except:
                #conn1.close()
                continue
            
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()

        if addr[1] not in client_list:
            client_list[addr[1]] = conn
            print(type(addr[1]))

        thread =threading.Thread(target=handle_client, args=(conn, addr, client_list))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] server is starting...")
start()