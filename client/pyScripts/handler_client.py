from format import *

def getOption():
    print("Enter your option:")
    choice = input()
    return choice

def reqArticle( sock, article_num  ):
    article_num = str(article_num)
    sock.sendall(bytes(article_num, 'utf-8'))

def getArticle( sock, width ):
    article = sock.recv(1024).decode("utf-8")
    display(article, width)
