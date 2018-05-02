
import socket
import sys
import json
import datetime
from Tkinter import *
from threading import Thread




username = str(sys.argv[1])



def setDate():
    currentDatetime = datetime.datetime.now()
    currentDatetime.strftime("%Y-%m-%d %H:%M:%S")
    currentDatetime.isoformat()
    return str(currentDatetime)


def receiving():
    while True:
        # Receving
        try:
            message = server.recv(2048)
            newMessage = json.loads(message)
            if 'isConnected' in newMessage:
                isConnected = newMessage['isConnected']
                errorCode = newMessage['errorCode']
                if errorCode is 1:
                    server.close()
                    print 'username taken please try agian'
                    window.destroy()
                    sys.exit()
                elif errorCode is 2:
                    print 'server full please try agian later'
                    server.close()
                    window.destroy()
                    exit()
                elif isConnected is False:
                    print 'disconnected from server'
                    server.close()
                    window.destroy()
                    exit()

            elif 'dm' in newMessage:
                sender = newMessage['sender']
                dm = newMessage['dm']
                message = newMessage['message']
                length = int(newMessage['length'])
                date = newMessage['date']
                # jsonMessage = server.recv(2048)
                messageList.insert(END, '<%s>: %s\n' % (sender, message))
        except:
            continue


def sending(event):
    message = input_field.get()
    dm = inputDM.get()
    messageList.insert(END, "<%s>: %s" % (username, message))
    server.send(json.dumps({'dm': dm, 'sender': username, 'message': message, 'length': len(message), 'date': setDate() }))
    input_user.set('')
    return "break"


def onDisconnect():
    server.send(json.dumps({'disconnect': True, 'sender' : username}))
    window.destroy()
    server.close()
    exit()
    sys.exit()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.connect(('yetti.hopto.org',1134))
server.connect(('localhost',1134))

window = Tk()
window.title("Cool Chat Room Name")
frame = Frame(window)
scrollbar= Scrollbar(frame)


messageList = Listbox(frame,height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
messageList.pack(side=LEFT, fill=BOTH)
messageList.pack()

frame.pack()

labelDMText=StringVar()
labelDMText.set("DM:")
labelDM = Label(window, textvariable=labelDMText)
inputDM = StringVar()
inputDMField = Entry(window, textvariable=inputDM)
labelDM.pack(side=LEFT)
inputDMField.pack(side=LEFT)

messageLabelText = StringVar()
messageLabelText.set("Message:")
messageLabel = Label(window, textvariable=messageLabelText)
input_user = StringVar()
input_field = Entry(window, textvariable=input_user)
messageLabel.pack(side=LEFT)
input_field.pack(side=LEFT)

input_field.bind("<Return>", sending)

disconnectButton = Button(window, text="Disconnect", command=onDisconnect)
disconnectButton.pack(side=BOTTOM)
frame.pack()

receive_thread = Thread(target=receiving)
receive_thread.start()
server.send(json.dumps({'username':username}))




mainloop()
