import socket
import time
import threading

PORT = 5050
SEVER = socket.gethostbyname(socket.gethostname())
ADDR = (SEVER,PORT)
FORMAT = "utf-8"
HEADER = 64
DISCONNET = "disconnect"

sever = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sever.bind(ADDR)

def handle_client(conn,addr):
    """This functions is reposible for 
    handling the client msg to the sever and 
    also cleaning it or closing the sever link when the
    user disconnects.
    """
    print(f"[NEW CONNECTION]: {addr} connected.")
    connected = True
    while connected:
        msg_lenght = conn.recv(HEADER).decode(FORMAT)
        if msg_lenght:
            msg_lenght =  int(msg_lenght)
            msg  =  conn.recv(msg_lenght).decode(FORMAT)
            if msg == DISCONNET:
                connected = False
                print(f"{addr} disconnected!")

            print(f"{addr}: {msg}")
    conn.close()


def start():
    """ Initialize the sever connection to 
    the client.
    """
    sever.listen()
    print(f"[SEVER IP] : {SEVER}")
    bool = True
    while bool:
        conn, addr = sever.accept()
        thread = threading.Thread(target=handle_client ,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE USER]:{threading.active_count()-1}")


print("SEVER IS ON!")
start()
