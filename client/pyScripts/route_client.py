from handler_client import *

def route(sock, option, SIZE):

    option = int(option)
    sendData(sock, option)

    if option == 1:
        article_num = getArticleNum()
        reqArticle(sock, article_num)

        getAnnotation(sock, SIZE)

        getArticle(sock, SIZE)

    elif option == 2:
        tags = getTags(sock)
        showTags(tags)
        tags = selectTags(tags)
        getArticleIDByTags(sock, tags)
        tags = getTags(sock)
        getArticleByTags(sock, tags, SIZE)

    elif option == -1:
        sock.close()
        print("Closing Connection and Exitting")
        exit(1)

    else:
        showOption()