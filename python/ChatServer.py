import SocketServer
import SimpleHTTPServer
import socket
import sys
import Broadcast
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
connectionList = {}
while True:
    client, client_addressess = serverSocket.accept()
    addressess[client] = client_addressess
    start_new_thread(target=Connection(client, connectionList), args=(client,)).start()
    start_new_thread(target=Broadcast(connectionList)).start()




#if __name__ == '__main__':
#   print 'Waiting for connections...'

