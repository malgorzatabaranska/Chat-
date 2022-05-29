# Aplication for Chatting 
# Aplication send masseges betwen two chatbox window and using local Server
# Every messages are archive in Data Base (PostgreSQL)

from email import message
from socket import *
        

class Client(object): 
    """ Client chatbox window"""

    SERVER_ADRESS = "127.0.0.1"
    PORT_SERVER = 10000
    nick = input("Wprowadź swój nick: ")

    def __init__(self):
        self.connection()


    def connection(self):
        #create socket
        self.c = socket(AF_INET, SOCK_STREAM)
        #connect to server 
        self.c.connect((self.SERVER_ADRESS, self.PORT_SERVER))
        self.c.send(self.nick.encode('ascii'))
        welcome = self.c.recv(2048).decode('ascii')
        print(welcome)
        self.input_message()

    
    def input_message(self):
        """gets form user messages"""
        nick = self.nick
        self.user_message = input('')
        self.send_massage(nick, self.user_message)


    def from_user_reciving(self):
        # Recive message from User        
        while True: 
            message_form_user = self.c.recv(2048)
            print(message_form_user)
            self.input_message()
            

    def send_massage(self, nick, mgs):
        while True: 
            message = (nick  + ":" + mgs)
            print("\x1b[1;36;40m{}\x1b[0m {}".format("You", self.user_message))
            self.c.send(message.encode('ascii'))
            self.from_user_reciving()         
            

#class Window(object):
    #"""Using UGI Interface to print all messages"""
    # Reciving from Server
        # messages
        # Nick


def main():
    client= Client()
   # box = Window(client_user)
  

main()







        





