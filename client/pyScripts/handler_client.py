import os

def showOption():
    print("1.Request article number\n2.Request article by tags\n-1.Exit")

def getOption():
    print();
    choice = input("Enter your option:")
    return choice

def getSize():
    term_size = os.get_terminal_size()
    size = str(term_size)

    width = int(size[size.find("=")+1: size.find(",")])

    return width


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
            continue
        if name not in tag:
            tag.append(name)
        name = input("Enter the names of tags:")

    return tag

def getArticleIDByTags( sock, tags ):
    sendData(sock, tags)

def getArticleByTags( sock, tags, width ):
    n = int(len(tags)/5)
    print("\n----------------------------------------------------\----------------------------------------------------\n")

    for id in range(n):
        reqArticle(sock, tags[id])
        getArticle(sock, width)
        getArticle(sock, width)
        print("\n----------------------------------------------------\----------------------------------------------------\n")

    return
