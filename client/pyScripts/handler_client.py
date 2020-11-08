import os

def showOption():
    print("10.Request article number\n14.Request article by tags\n22.List\n30.WhoamI\n-1.Exit")

def getOption():
    print();
    choice = input("Enter your option:")
    return choice

def getSize():
    term_size = os.get_terminal_size()
    size = str(term_size)

    width = int(size[size.find("=")+1: size.find(",")])

    return width

def getStatus(sock):
    status = sock.recv(1024).decode("utf-8")
    print(status)
    return status[2:5]

def display(string, width):
    print("\n" + string.center(width))

def sendData(sock, data):
    send_option = str(data)
    sock.sendall(bytes(send_option, 'utf-8'))

def reqArticle( sock, article_num  ):
    article_num = str(article_num)
    sock.sendall(bytes(article_num, 'utf-8'))

def getArticleNum():
    article_num = input("Enter the article number:")
    return article_num

def getAnnotation(sock, width):
    article = sock.recv(1024).decode("utf-8")
    display(article, width)

def getArticle( sock, width ):
    article = sock.recv(1024).decode("utf-8")
    display(article, width)

def getTags(sock):
    tags = sock.recv(1024).decode("utf-8")
    return tags

def showTags(tags):
    print(tags)

def selectTags(tags):
    name = 1
    print("Enter -1 to stop entering tags")

    tag = []
    name = input("Enter the names of tags:")

    while name != "-1":
        if name not in tags:
            print("Incorrect tag entered")
            break
        if name not in tag:
            tag.append(name)
        name = input("Enter the names of tags:")

    return tag

def reqArticleIDByTags( sock, tags ):
    sendData(sock, tags)

def getArticleByTags( sock, tags, width ):

    if int(getStatus(sock)) < 300:
        print("\n----------------------------------------------------\----------------------------------------------------\n")

        n = int(len(tags)/5)

        for id in range(n):
            reqArticle(sock, tags[id])
            getArticle(sock, width)
            getArticle(sock, width)
            print("\n----------------------------------------------------\----------------------------------------------------\n")

    return


def showArticleIDByTags(sock, tags):
    if int(getStatus(sock)) < 300:
        print("\nTHE LIST ARTICLES ARE:" + tags)
    return

def getLogin():
    print();
    usrname = input("Enter your usrname:")
    pwd = input("Enter your pwd:")

    loginDet = usrname +":"+ pwd
    return loginDet


def sendArticle(conn, article_num):
    with open('../data/article/' + str(article_num) + ".txt", 'r') as data:
        data = data.read()

    sendData(conn, data)


def sendAnnotation(conn, article_num):
    with open('../data/annotation/' + str(article_num) + ".json", 'r') as data:
        data = data.read()

    sendData(conn, data)
