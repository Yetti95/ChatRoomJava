import SocketServer
import SimpleHTTPServer
import socket
import sys
import Broadcast
import Connection
import threading

#class ChatServer:
HOST = ''
PORT = 1134
SOCKET_LIST = []
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind((HOST, PORT))
serverSocket.listen(10)
connectionList = {}
broad = Broadcast
bt = threading.Thread(target=broad.run, args=(broad, connectionList,))
bt.start()

while True:
    client, client_addressess = serverSocket.accept()
    #What is addressess? what does it do?
    con = Connection
    t = threading.Thread(target=con.run, args=(client, connectionList))
    t.start()
    #start_new_thread(target=Broadcast(connectionList)).start()




#if __name__ == '__main__':
#   print 'Waiting for connections...'

