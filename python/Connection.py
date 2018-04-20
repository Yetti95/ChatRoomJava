import Handler
import json
import Broadcast

connectionsList = {'username', 'client'}
request = json
previousMessage = ()

def run(self, Socket, connectionList):
    client = Socket
    self.connectionsList = connectionsList
    handler = Handler.__init__(client)
    handler.read()
    username = handler.getUsername()

    #adds our client to the list of connections
    if(self.connectionsList.count == 0):
        self.connectionsList.append((username, client))
    else:
        if username is not '':

            #we do not allow multiple of the same username
            if(self.connectionsList.__contains__(username)):

                self.request = handler.nameTaken() #type: JSON
                self.sendMessage(self.request)
                return
            else:
                self.connectionsList.append((username, client))
                self.sendMessage(handler.onJoin())


    # here is where we need to check against a vector to see if the message being sent is a new message or not
    # I think the best way to do that is have a tuple of (username, message)
    # if (handler.getUsername(), handler.getMessage) is previousTuple then do nothing
    # else send the message to broadcast
    if (handler.getUsername(), handler.getMessage()) is not previousMessage:
        message = (handler.getUsername(), handler.getMessage())
        Broadcast.setMessage(message)
        self.previousMessage = message





    #I think dm will be hard. it is extra credit
    #if handler.getDm() not empty then send to individual clients based on @username
    #else do nothing



    return

def sendMessage(self, JSON):
    #this will take a json object and send it the bt


    return
