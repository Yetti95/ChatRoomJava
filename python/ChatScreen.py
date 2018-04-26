import socket
import select
import sys
import json
from thread import *
import datetime

onJoin = {}
toSend = {}

def setDate():
    currentDatetime = datetime.datetime.now()
    currentDatetime.strftime("%Y-%m-%d %H:%M:%S")
    currentDatetime.isoformat()
    return str(currentDatetime)


def recieving(username, server):
    while True:

        # maintains a list of possible input streams
        sockets_list = [sys.stdin, server]
        """ There are two possible input situations. Either the
        user wants to give  manual input to send to other people,
        or the server is sending a message  to be printed on the
        screen. Select returns from sockets_list, the stream that
        is reader for input. So for example, if the server wants
        to send a message, then the if condition will hold true
        below.If the user wants to send a message, the else
        condition will evaluate as true"""
        read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])


        # Receving
        try:
            message = server.recv(2048)
            print message
            newMessage = json.loads(message)
            if 'isConnected' in newMessage:
                isConnected = newMessage['isConnected']
                errorCode = newMessage['errorCode']
                if errorCode is 1:
                    server.close()
                    print 'username taken please try agian'
                    exit()
                elif errorCode is 2:
                    print 'server full please try agian later'
                    server.close()
                    exit()
                elif isConnected is False:
                    print 'disconnected from server'
                    server.close()
                    exit()

            elif 'dm' in newMessage:
                sender = newMessage['sender']
                if sender is '':
                    sender = 'server'
                dm = newMessage['dm']
                message = newMessage['message']
                length = int(newMessage['length'])
                date = newMessage['date']
                # print '<%s> %s\n', sender, message
                sys.stdout.write(sender)
                sys.stdout.write(message)
                sys.stdout.flush()
            else:
                if 'disconnected' in newMessage:
                    disconnected = newMessage['disconnected']
        except:
            continue
            #sending

def sending(username, server):
    while True:
        try:
            tempString = sys.stdin.read()
            message = str(tempString)
            if message is 'exit()':
                #server.close()
                print 'close'
            else:

                print 'sending'
                temp = {}
                temp['dm'] = ''
                temp['message'] = message
                temp['sender'] =  username
                temp['length'] = len(message)
                temp['date'] = setDate()
                #temp = json.loads(''''{'dm' : '', 'message' : message, 'sender' : username, 'length' : len(message), 'date' = setDate()}''')
                obj = json.loads(temp)
                print obj
                server.send(obj)
        except:
            continue
        #temp = "{'dm' = '', 'message' = " + message + ", 'sender' = " + username + "'length' = " + str(len(message)) + "'date' = " + str(setDate())
        #returnString = "{'dm' = '', 'message' = %s, 'sender' = %s, length' = %d, 'date' = %s}", message, username, len(message), setDate()
    #sys.stdout.write("<You>")
    #sys.stdout.write(message)
    #sys.stdout.flush()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print "Correct usage: script, IP address, username"
    print "Username cannot have a space"
    exit()
"""
Write two threads for the client that way you can read and write at the same time
"""
IP_address = str(sys.argv[1])
Port = 1134
username = str(sys.argv[2])
server.connect((IP_address, Port))
server.setblocking(True)
onJoin['username'] = username
temp = json.dumps(onJoin)
server.send(temp)
start_new_thread(sending,(username,server))
start_new_thread(recieving,(username,server))
