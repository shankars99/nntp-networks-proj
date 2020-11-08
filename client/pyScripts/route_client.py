from handler_client import *

def route(sock, option, SIZE):

    option = int(option)
    sendData(sock, option)

    if option == 10:
        article_num = getArticleNum()
        reqArticle(sock, article_num)

        getAnnotation(sock, SIZE)

        getArticle(sock, SIZE)

    elif option == 14:
        tags = getTags(sock)
        showTags(tags)
        tags = selectTags(tags)
        reqArticleIDByTags(sock, tags)
        tags = getTags(sock)
        getArticleByTags(sock, tags, SIZE)

    elif option == 22:
        tags = getTags(sock)
        showTags(tags)
        tags = selectTags(tags)
        reqArticleIDByTags(sock, tags)
        tags = getTags(sock)
        showArticleIDByTags(sock, tags)

    elif option == 30:
        loginDet = getLogin()
        reqArticleIDByTags(sock, loginDet)
        if int(getStatus(sock)) > 300:
            return
        article_num = getArticleNum()
        sendAnnotation(sock, article_num)
        sendArticle(sock, article_num)

    elif option == -1:
        sock.close()
        print("Closing Connection and Exitting")
        exit(1)

    else:
        showOption()
