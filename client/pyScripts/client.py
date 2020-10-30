#%%
import socket
import os


from format import *
from route_client import *
from handler_client import *
#%%
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
SIZE = getSize()
#%%
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    while True:
        choice = getOption()
        route(sock, choice, SIZE)

# %%
