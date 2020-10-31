from handler_server import *

def route(conn, option, telnet):
    if option[0] == '[':
        return
    option = int(option)

    if option == 1:
        article_num = getArticleNum(conn, telnet)
        sendAnnotation(conn, article_num)
        sendArticle(conn, article_num)

    elif option == 2:
        tags = readTags()
        sendTags(conn, tags)
        tags = getListOfTags(conn)
        idList = getIDList(tags)
        sendTags( conn, idList)
        sendArticlesByTag( conn, idList)

    elif option == -1:
        conn.close()
        print("Quitting")
