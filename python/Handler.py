import json
import socket
import datetime

client = socket  # type: object
username = ''
isConnected = False
errorCode = 0
disconnected = False
dm = ''
message = ''
length = 0
date = ''
sender = ''

def __init__(self, Socket):
    self.client = Socket

def read(self):
    temp = self.client.recv(2048)
    self.toString(self, temp)

def toJSON(self, String):
    messageObj = json.dumps(String)
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
                self.sender = newMessage['sender']
                self.message = newMessage['message']
                self.length = int(newMessage['length'])
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

def setLength(self, message):
    self.length = len(message)

def setDate(self):
    #YYYY-MM-DD-HH-mm-SS
    year = datetime.date.year
    month = datetime.date.month
    day = datetime.date.day
    hour = datetime.time.hour
    minute = datetime.time.minute
    second = datetime.time.second

    self.date = '%s-%s-%s-%s-%s-%s', year, month, day, hour, minute, second

def messageToJSON(self, username, message):
    self.username = username
    self.message = message
    returnString= '''
    {
        'dm' = '',
        'message' = %s,
        'sender' = %s,
        'length' = %d,
        'date' = %s
    }
    ''', self.message, self.sender, self.setLength(self, self.message), self.setDate(self)

    return self.toJSON(self, returnString)



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

#this compiles the response to someone joining the chat room

def onJoin(self):
    self.setDate(self)
    returnStatus = '''
    {
        'dm' : ,
        'message' : '%s has entered the chat'
        'length' : '$d'
        'date'  :   '%s'
        
    }
    ''', self.username, self.length, self.date
    status = json.dumps(returnStatus)
    #should this return string or json?
    return status
