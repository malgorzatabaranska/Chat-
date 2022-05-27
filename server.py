from socket import *
from threading import Thread
import threading


#"""Server is  using for communicate betwen two Users"""

# Sending and reciving:
    # messages 
        # User - Server - User 
        # User - Server - Data Base - Server(future)

IP_SERVER = ""
PORT_SERVER = 10000

  
soc = socket(AF_INET, SOCK_STREAM)
soc.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
soc.bind((IP_SERVER, PORT_SERVER))
soc.listen(10)
list_of_clients = []
thread = []


def client(c, addr):
    c.send(("Welcome to chatroom!").encode('utf-8'))
    while True:
        try:
            message = c.recv(2048)
            if message:
                message_to_send = message
                broadcast(message_to_send, c)
            else: 
                remove(c)
        except: 
            continue
        


def broadcast(message, connection):
    """Using the below function, we broadcast the message to all
    clients who's object is not the same as the one sending
    the message """
    for clients in list_of_clients: 
        if clients != connection:
            try:
                clients.send(message)
            except: 
                clients.close()
                remove(clients) 

    
def remove(connection):
    """The following function simply removes the object
    from the list that was created"""
    if connection in list_of_clients:
        list_of_clients.remove(connection)


while True:
 
    """Accepts a connection request and stores two parameters,
    conn which is a socket object for that user, and addr
    which contains the IP address of the client that just
    connected"""
    conn, addr = soc.accept()

    thread_client = threading.Thread(target = client, args=(conn, addr))
    thread.append(thread_client)
    thread_client.start()
    list_of_clients.append(conn)
  

for t in thread_client:
    t.join()

conn.close()
server.close()

        

    #def server_sending_db(self, message):

        #wysyłka wiadomości do DB- jeszcze nie wiem jak

        #wysylka wiadomości do okna
        #self.message_to_send = message.server_message
   