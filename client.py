import socket
from time import sleep
from threading import Thread

# server config --------------------

FORMAT          = 'utf-8'
IP, PORT        = input('Enter server address like: 192.168.1.36:8000 \n').split(':')
SERVER_ADDRESS  = (IP, int(PORT))
client          = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    name = input('Your name: ')
    client.connect(SERVER_ADDRESS)
    print('CONNEDTED TO THE SERVER!')

except Exception as e:
    print(e)
    sleep(2)
    exit()


def send():
    while True:
        msg = input()
        client.send((name + ': ' + msg).encode(FORMAT))


def receive():
    while True:
        msg = client.recv(1024)
        print(msg.decode(FORMAT))


Thread(target=send, args=()).start()
receive()

