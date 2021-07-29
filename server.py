import socket
from time import sleep
from threading import Thread

# server config --------------------

PORT            = 8000
IP              = '192.168.1.36'
SERVER_ADDRESS  = (IP, PORT)
server          = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connections     = set()

try:
    server.bind(SERVER_ADDRESS)
    server.listen()
    print(f'SERVER IS LISTENING ON: {SERVER_ADDRESS}')
except Exception as e:
    print(e)
    sleep(2)
    exit()


def client_handle(connection, address):
    while True:
        msg = connection.recv(1024)
        if msg: 
            for c in connections:
                if c != connection:
                    c.send(msg)

        else:
            print(f'DISCONNECTED: {address}')
            connections.remove(connection)
            print(f'CONNECTED: {len(connections)}')
            break


while True:
    connection, address = server.accept()
    connections.add(connection)

    print(f'CONNECTED: {address}')
    print(f'CONNECTED: {len(connections)}')

    Thread(target=client_handle, args=(connection, address)).start()
