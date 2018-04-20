import Handler
import json

connectionsList = {'username', 'client'}
request = json

def run(self, Socket):
    client = Socket
    handler = Handler.__init__(client)
    handler.read()
    username = handler.getUsername()

    #adds to our client to the list of connections
    if(self.connectionsList.count == 0):
        self.connectionsList.append((username, client))
    else:
        #we do not allow multiple of the same username
        if(self.connectionsList.__contains__(username)):

            self.request = handler.nameTaken() #type: JSON
            self.sendMessage(self.request)
            return
        else:
            self.connectionsList.append((username, client))

     #here is where we need to check against a vector to see if the message being sent is a new message or not
    #I think the best way to do that is have a tuple of (username, message)
    #if (handler.getUsername(), handler.getMessage) is previousTuple then do nothing
    #else send the message to broadcast




    #I think dm will be hard. it is extra credit
    #if handler.getDm() not empty then send to individual clients based on @username
    #else do nothing



    return

def sendMessage(self, JSON):
    #this will take a json object and send it the client


    return

