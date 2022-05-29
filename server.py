

from datetime import datetime
from socket import *
from threading import Thread
import threading
import psycopg2


class Server(object):

    #"""Server is  using for communicate betwen two Users"""

    # Sending and reciving:
    # messages 
        # User - Server - User 
        # User - Server - Data Base - Server(future)

    IP_SERVER = ""
    PORT_SERVER = 10000 


    def __init__(self):
        self.list_of_clients = []
        self.thread = []
        self.nick = []
        self.connection()


    def connection(self):
        self.soc = socket(AF_INET, SOCK_STREAM)
        self.soc.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.soc.bind((self.IP_SERVER, self.PORT_SERVER))
        self.soc.listen(10)
        self.running()
        

    def client(self, c, a):
        c.send(("Welcome to chatroom!").encode('ascii'))
        while True:
            try:
                message = c.recv(2048)
                if message:
                    message_to_send = message
                    self.broadcast(message_to_send, c)
                else: 
                    self.remove(c)
            except: 
                continue
        


    def broadcast(self, message, connection):
        """Using the below function, we broadcast the message to all
        clients who's object is not the same as the one sending
        the message """
        for clients in self.list_of_clients: 
            if clients != connection:
                try:
                    clients.send(message)
                   # Database.send_data(self.user, message)
                except: 
                    clients.close()
                    self.remove(clients) 

    
    def remove(self, connection):
        """The following function simply removes the object
        from the list that was created"""
        if connection in self.list_of_clients:
            self.list_of_clients.remove(connection)
            index = self.list_of_clients(connection)
            nickname = self.nick[index]
            self.nick.remove(nickname)


    def running(self):
        while True:
 
            """Accepts a connection request and stores two parameters,
            conn which is a socket object for that user, and addr
            which contains the IP address of the client that just
            connected"""
            conn, addr = self.soc.accept()
            self.user = conn.recv(2048)
            self.nick.append(self.user)
            thread_client = threading.Thread(target=self.client, args=(conn, addr))
            self.thread.append(thread_client)
            thread_client.start()
            self.list_of_clients.append(conn)
  

        for t in thread_client:
            t.join()

        self.conn.close()
        self.soc.close()


class Database(object):
    #Database in POSTGRESQL is responsible for sending and archive
    #data (Nick, massage and date)
   

    def connection(self):
        self.conn = psycopg2.connect("dbname='pyapp' user='gosia' password='123'")

    def send_data(self, user, message):
        nick = user
        data = message
        cur =  self.conn.cursor()

        try: 
            cur.execute("INSERT INTO achive(nick,message,date) VALUES(%s, %s)", (nick, data, datetime))
        except: 
            print("Failed to insert data in achive table") 
    
   
def main():

    sv = Server() 
    db = Database(sv)

main()