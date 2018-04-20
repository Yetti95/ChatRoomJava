import json
import socket

client = socket  # type: object
username = ''
isConnected = False
errorCode = 0
disconnected = False
dm = ''
message = ''
length = 0
date = ''

def __init__(self, Socket):
    self.client = Socket

def read(self):
    temp = self.client.recv(2048)
    self.toString(self.toJSON(temp))

def toJSON(self, String):
    messageObj = json.dumps(String, str='utf-8')
    return messageObj

#parses the data in regular values
def toString(self, JSON):
    newMessage = json.loads(JSON)
    if 'username' in newMessage:
        self.username = newMessage['username']
    else :
        if 'isConnected' in newMessage:
            self.isConnected = newMessage['isConnected']
            self.errorCode = newMessage['errorCode']
        else:
            if 'dm' in newMessage:
                self.dm = newMessage['dm']
                self.message = newMessage['message']
                self.length = newMessage['length']
                self.date = newMessage['date']
            else:
                if 'disconnected' in newMessage:
                    self.disconnected = newMessage['disconnected']
    return newMessage

def getUsername(self):
    return self.username

def getIsConnected(self):
    return self.isConnected

def getErrorCode(self):
    return self.errorCode

def getDisconnected(self):
    return self.disconnected

def getDM(self):
    return self.dm

def getMessage(self):
    return self.message

def getLength(self):
    return self.length

def getDate(self):
    return self.date


def nameTake(self):
    self.errorCode = 1
    self.isConnected = False
    returnStatus = '''
    {
        'isConnected' : false,
        'errorCode' : 1
    }
    '''
    status = json.loads(returnStatus, 'utf-8')
    return status
