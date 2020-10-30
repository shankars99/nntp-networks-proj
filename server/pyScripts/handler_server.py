import json
from types import SimpleNamespace

def getArticle( conn ):
    data = conn.recv(1024).decode()
    print(data)
    data = str(data)
    data = data[0:data.find("\r")]

    telnet = 1
    if data == -1:
        telnet = 0

    return data,telnet

def sendData( conn, data):
    annotation = bytes(data, "utf-8")
    conn.sendall(annotation)


def sendArticle( conn, article_num):
    with open('../articles/article/' + str(article_num) + ".txt", 'r') as data:
        data = data.read()

    sendData(conn, data)


def sendAnnotation( conn, article_num ):
    with open('../articles/annotation/' + str(article_num) + ".json", 'r') as data:
        data = data.read()

    sendData(conn, data)
