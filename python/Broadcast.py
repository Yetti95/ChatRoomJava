import json
import Handler
previousMessage = ()
message = None
handle = Handler
def run(self, connectionList):
    if previousMessage is not message:
        for client in connectionList:
            self.sendMessage(self, client)

def setMessage(self, (username, message)):
    self.message = (username, message)

def sendMessage(self, client):
    client.send(handle.messageToJSON(handle, message))

