import os

def getSize():
    term_size = os.get_terminal_size()
    size = str(term_size)

    width = int(size[size.find("=")+1: size.find(",")])

    return width

def display( string, width ):
    print(string.center(width))
