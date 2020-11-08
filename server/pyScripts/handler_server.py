import json
import os
import pickle
from types import SimpleNamespace

def getOption(conn):
    option = conn.recv(1024).decode()

    telnet = 0

    if option.find("\r") > 0:
        option = option[0:option.find("\r")]
        telnet = 1

    return option, telnet


def sendData(conn, data):
    annotation = bytes(data, "utf-8")
    conn.sendall(annotation)

def getArticleNum( conn , telnet):
    data = conn.recv(1024).decode()

    data = str(data)

    if telnet == 1:
        data = data[0:data.find("\r")]

    return data

def sendStatus(conn, data):
    status = ""
    code = 200

    if len(data) > 0:
        status = "\n[200] Successful"
    else:
        status = "\n[400] Failed"
        code = 400
    data = bytes(status, "utf-8")
    conn.sendall(data)
    return code

def sendArticle(conn, article_num):
    with open('../articles/article/' + str(article_num) + ".txt", 'r') as data:
        data = data.read()

    sendData(conn, data)


def sendAnnotation( conn, article_num ):
    with open('../articles/annotation/' + str(article_num) + ".json", 'r') as data:
        data = data.read()

    sendData(conn, data)


def sendTags(conn, tags):
    tags = str(tags)
    print(tags)
    sendData(conn, tags)


def readTags():
    files = os.listdir("../articles/annotation")
    tags = []

    with open('../data/tags.p', 'rb') as data:
        if len(data.read()) > 0:
            data = pickle.load(open('../data/tags.p', 'rb'))

    for i in files:
        with open('../articles/annotation/' + i, 'r') as data:
            x = json.loads(data.read(), object_hook=lambda d: SimpleNamespace(**d))
            for j in x.tags:
                if j not in tags:
                    tags.append(j)


    pickle.dump(tags, open('../data/tags.p', 'wb'))
    return(tags)

def getListOfTags( conn ):
    tags = conn.recv(1024).decode("utf-8")
    return tags


def getIDList(tags):
    files = os.listdir("../articles/annotation")
    id = []

    data = pickle.load(open('../data/tags.p', 'rb'))

    for i in files:
        with open('../articles/annotation/' + i, 'r') as data:
            x = json.loads(data.read(), object_hook=lambda d: SimpleNamespace(**d))
            for j in x.tags:
                if j in tags:
                    id.append(x.number)

    return(id)

def sendArticleName(conn, id):
    with open('../articles/annotation/' + str(id) + ".json", 'r') as data:
        x = json.loads(data.read(), object_hook=lambda d: SimpleNamespace(**d))
        sendData(conn, x.title)

def sendArticlesByTag(conn, idList):
    for id in idList:
        sendArticleName(conn, id)
        sendArticle(conn, id)

    return

def findArticle(article_num):
    files = os.listdir("../articles/annotation")

    for file in files:
        with open('../articles/annotation/' + file, 'r') as data:
            x = json.loads(data.read(), object_hook=lambda d: SimpleNamespace(**d))
            if x.number == article_num:
                return 200

    return ""

def checkAuth(conn, tags):
    data = pickle.load(open('../data/auth.p', 'rb'))

    usrname = tags[:tags.find(':')]
    pwd = tags[tags.find(':') + 1:]

    if usrname not in data or data[usrname] != pwd:
        return sendStatus(conn, "")
    else:
        return sendStatus(conn, "200")


def getAnnotation(sock):
    article = sock.recv(1024).decode("utf-8")
    f = open("../articles/raw-article/test-1.json", "w")
    f.write(article)
    f.close()
    #display(article)


def getArticle(sock):
    article = sock.recv(1024).decode("utf-8")
    f = open("../articles/raw-article/test-1.txt", "w")
    f.write(article)
    f.close()
    #display(article)


def display(string):
    print("\n" + string)
