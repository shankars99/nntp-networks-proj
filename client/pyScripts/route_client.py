from format import *
from handler_client import *

def route(sock, option, SIZE):

    if option == 1:
        reqArticle(sock, 107)

        getArticle(sock, SIZE)
        getArticle(sock, SIZE)
    else:
        pass
