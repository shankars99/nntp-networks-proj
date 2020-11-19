import socket
import os

from _thread import *
from handler_server import *
from route_server import *

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 42069
ThreadCount = 0

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen(5)


def threaded_client(conn):
    while True:
        option, telnet = getOption(conn)
        if not option:
            break
        route( conn, option, telnet )
    conn.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()










'''import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen()
        conn, addr = sock.accept()

        with conn:
            print('Connected by', addr)

            while True:
                option, telnet = getOption(conn)
                if not option:
                    break
                route( conn, option, telnet )

'''