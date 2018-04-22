import socket
import select
import sys
import json
import Handler

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print "Correct usage: script, IP address, username"
    print "Username cannot have a space"
    exit()

IP_address = str(sys.argv[1])
Port = 1134
username = str(sys.argv[2])
server.connect((IP_address, Port))
handle = Handler

request = '''
        {
            'username' : %s
        }
    
    ''', username
temp = json.dumps(request)
server.send(temp)


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

    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            handle.toString(handle, message)
            sys.stdout.write(handle.getSender(handle))
            sys.stdout.write(handle.getMessage(handle))
            sys.stdout.flush()
        else:
            message = sys.stdin.readline()
            jsonMessage = handle.messageToJSON(handle, username, message)
            server.send(jsonMessage)
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()
