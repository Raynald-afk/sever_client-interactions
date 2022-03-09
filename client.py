import socket

PORT = 5050
FORMAT = "utf-8"
HEADER = 64
DISCONNET = "disconnect"
SEVER = "192.168.43.186"
ADDR = (SEVER,PORT)


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER -len(send_length))
    client.send(send_length)
    client.send(message)




user = ""
while user != DISCONNET:
    user = input("Enter a message to send to the sever: ")
    send(user)

