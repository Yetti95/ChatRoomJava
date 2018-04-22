import Handler
import json
import Broadcast

connectionsList = {'username', 'client'}
request = json
previousMessage = ()

def run(Socket, connectionList):
    client = Socket
    handler = Handler
    handler.__init__(handler, client)
    handler.read(handler)
    username = handler.getUsername(handler)

    #adds our client to the list of connections
    if(connectionsList.__len__() == 0):
        connectionsList.append((username, client))
    else:
        if username is not '':

            #we do not allow multiple of the same username
            if(connectionsList.__contains__(username)):

                request = handler.nameTaken(handler) #type: JSON
                client.send(request)
                return
            else:
                connectionsList.append((username, client))
                client.send(handler.onJoin(handler))


    # here is where we need to check against a vector to see if the message being sent is a new message or not
    # I think the best way to do that is have a tuple of (username, message)
    # if (handler.getUsername(), handler.getMessage) is previousTuple then do nothing
    # else send the message to broadcast
    #message = (handler.getUsername(handler), handler.getMessage(handler))
    #Broadcast.setMessage(message)





    #I think dm will be hard. it is extra credit
    #if handler.getDm() not empty then send to individual clients based on @username
    #else do nothing
    if handler.getDM(handler) is not '':
        if connectionList.conations(handler.getDM(handler)):
            toClient = connectionList(handler.getDM(handler))
            toClient.send(handler.messageToJSON(handler, handler.getUsername(handler), handler.getMessage(handler)))


    return


