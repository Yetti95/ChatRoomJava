import json
import Handler
previousMessage = ()
message = ()
connectionList = {}
handle = Handler
def run(self, connectionList):
    self.connectionList = connectionList
    if previousMessage is not message:
        for client in connectionList:
            self.sendMessage(client)

def setMessage(self, (username, message)):
    self.message = (username, message)

def sendMessage(self, client):
    client.send(handle.messageToJSON())

