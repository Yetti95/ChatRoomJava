import socket
import select
import sys
import json
from threading import Thread
from thread import *
import datetime

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print "Correct usage: script, IP address, username"
    print "Username cannot have a space"
    exit()
onJoin = {}
toSend = {}
IP_address = str(sys.argv[1])
Port = 1134
username = str(sys.argv[2])
server.connect((IP_address, Port))
server.setblocking(True)
onJoin['username'] = username
temp = json.dumps(onJoin)
server.send(temp)

def setDate():
    currentDatetime = datetime.datetime.now()
    currentDatetime.strftime("%Y-%m-%d %H:%M:%S")
    currentDatetime.isoformat()
    return str(currentDatetime)


def receiving():
    print 'receiving thread started'
    while True:
        # Receving
        try:
            message = server.recv(2048)
            newMessage = json.loads(message)
            print "New message: ", newMessage
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
                sys.stdout.write(sender + ": ")
                sys.stdout.write(message)
                sys.stdout.flush()
            else:
                if 'disconnected' in newMessage:
                    disconnected = newMessage['disconnected']
        except:
            continue
            #sending

def sending():
    print 'sending Thread started'
    while True:
        try:
            tempString = sys.stdin.readline()
            message = str(tempString)
            if message is 'exit()':
                print 'close'
                server.close()
                break
            else:
                print 'sending'
                temp = {}
                temp['dm'] = ''
                temp['message'] = message
                temp['sender'] = username
                temp['length'] = len(message)
                temp['date'] = setDate()
                #temp = json.loads(''''{'dm' : '', 'message' : message, 'sender' : username, 'length' : len(message), 'date' = setDate()}''')
                obj = json.dumps(temp)
                # print obj
                server.send(obj)

        except:
            continue
    exit()

def test():
    while True:
        server.send("HI")

sendingThread = Thread(target=sending)
recievingThread = Thread(target=receiving)
try:
    sendingThread.start()
    recievingThread.start()
except (KeyboardInterrupt, SystemExit):
    cleanup_stop_thread()
    sys.exit()
