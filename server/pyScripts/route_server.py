from handler_server import *

def route(conn, option, telnet):
    if option[0] == '[':
        return
    option = int(option)

    if option == 10:
        article_num = getArticleNum(conn, telnet)
        sendAnnotation(conn, article_num)
        sendArticle(conn, article_num)

    elif option == 14:
        tags = readTags()
        sendTags(conn, tags)
        tags = getListOfTags(conn)
        idList = getIDList(tags)
        sendTags( conn, idList)
        sendArticlesByTag( conn, idList)

    elif option == 22:
        tags = readTags()
        sendTags(conn, tags)
        tags = getListOfTags(conn)
        idList = getIDList(tags)
        sendTags(conn, idList)
        sendStatus(conn, tags)

    elif option == -1:
        conn.close()
        print("Quitting")
