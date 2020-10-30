# %%
import socket

from handler_server import *
# %%
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
# %%

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen()
        conn, addr = sock.accept()

        with conn:
            print('Connected by', addr)

            while True:
                article_num, telnet = getArticle(conn)
                if not article_num:
                    break
                sendAnnotation(conn, article_num)
                sendArticle(conn, article_num)
# %%
1