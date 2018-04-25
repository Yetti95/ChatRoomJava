import socket
import select
import sys
import json
import datetime

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
# handle = Handler
# handle.__init__(handle, server)
# server.setblocking(False)
#server.settimeout()
request = "{ 'username' : %s }", username
temp = json.dumps(request)
server.send(temp)

def setDate():
    currentDatetime = datetime.datetime.now()
    currentDatetime.strftime("%Y-%m-%d %H:%M:%S")
    currentDatetime.isoformat()
    return str(currentDatetime)

#we need a seperate handler I think
#this way we can parse and act on the parsed information
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
        else:
            if 'dm' in newMessage:
                sender = newMessage['sender']
                if 'sender' is '':
                    sender = 'server'
                dm = newMessage['dm']
                message = newMessage['message']
                length = int(newMessage['length'])
                date = newMessage['date']
                sys.stdout.write(sender)
                sys.stdout.write(message)
                sys.stdout.flush()
            else:
                if 'disconnected' in newMessage:
                    disconnected = newMessage['disconnected']
    except:
        continue
            #sending
    try:
        tempString = sys.stdin.readline()

        message = str(tempString)
        if message is 'exit()':
            server.close()
        else:

            print 'sending'
            temp = {}
            temp['dm'] = ''
            temp['message'] = message
            temp['sender'] =  sender
            temp['length'] = len(message)
            temp['date'] = setDate()
            #temp = json.loads(''''{'dm' : '', 'message' : message, 'sender' : username, 'length' : len(message), 'date' = setDate()}''')
            obj = json.loads(temp)
            print obj
            server.send(temp)
    except:
        continue
        #temp = "{'dm' = '', 'message' = " + message + ", 'sender' = " + username + "'length' = " + str(len(message)) + "'date' = " + str(setDate())
        #returnString = "{'dm' = '', 'message' = %s, 'sender' = %s, length' = %d, 'date' = %s}", message, username, len(message), setDate()
    #sys.stdout.write("<You>")
    #sys.stdout.write(message)
    #sys.stdout.flush()



