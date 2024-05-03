import socket

HEADER =  64
PORT = 65432        # כתובת הפורט לתקשורת
FORMAT = 'utf-8'
DICONCONNECTED_MESSAGE = "!DICONCONNECET"
SERVER = '192.168.68.67' # כתובת IP של השרת
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)


def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg =conn.recv(msg_length).decode(FORMAT)
            if msg == DICONCONNECTED_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
00


def send(msg):
    massage = msg.encod(FORMAT)
    msg_length = len(massage)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(massage)

send(print("hi"))