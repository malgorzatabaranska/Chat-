# Aplication for Chatting 
# Aplication send masseges betwen two chatbox window and using local Server
# Every messages are archive in Data Base (PostgreSQL)

from socket import *


class User(object):
    """Class for User"""
    # Gets User Name (Nick)
    

    def __init__(self):
        self.nick = input("Wprowadź swój nick: ")
        

class Client(object): 
    """ Client chatbox window"""

    SERVER_ADRESS = "127.0.0.1"
    PORT_SERVER = 10000

    def __init__(self, user):
        self.connection()


    def connection(self):
        #create socket
        self.c = socket(AF_INET, SOCK_STREAM)
        #connect to server 
        self.c.connect((self.SERVER_ADRESS, self.PORT_SERVER))
        welcome = self.c.recv(2048).decode('utf-8')
        print(welcome)
        self.input_message()
    
    def input_message(self):
        """gets form user messages"""
        self.user_message = input("Wprowadż wiadomość: ")
        
        self.send_massage(self.user_message)


    def from_user_reciving(self):
        # Recive message from User        
        while True: 
            
            message = self.c.recv(2048)
            print(message)
            self.input_message()


    def send_massage(self, message):
        while True: 
            user_message = message
            print("\x1b[1;36;40m{}\x1b[0m {}".format(" You " , user_message))
            self.c.send((user_message).encode('utf-8'))
            self.from_user_reciving()
            
            

#class Window(object):
    #"""Using UGI Interface to print all messages"""
    # Reciving from Server
        # messages
        # Nick
    # Printing date messages in Users windows  
    #def __init__(self, sv_message):
     #   self.message = sv_message.message_to_send
      #  self.text_window(self.message)


    
    #def text_window(self, message):
     #   update_message = message
      #  print(update_message)
        


class Aplication(object):
    "Apliction"

    def __init__(self, user1):
        client_user1 = Client(user1)
       
       

def main():
    app_user = User()
   # box = Window(client_user)
    app = Aplication(app_user)

main()







        





