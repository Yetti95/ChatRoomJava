import SocketServer
import SimpleHTTPServer
import socket
import sys
import Connection
from thread import *

#class ChatServer:
HOST = ''
PORT = 1134
SOCKET_LIST = []
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind((HOST, PORT))
serverSocket.listen(10)

while True:
    client, client_addressess = serverSocket.accept()
    addressess[client] = client_addressess
    start_new_thread(target=Connection(client), args=(client,)).start()



#if __name__ == '__main__':
#   print 'Waiting for connections...'

