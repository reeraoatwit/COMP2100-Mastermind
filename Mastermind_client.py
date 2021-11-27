# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 16:03:45 2021

"""

import socket
import sys



def client():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = socket.gethostname() # Update before each use
    PORT = 9999
    try:
        clientsocket.connect((HOST, PORT))
    except (InterruptedError, TimeoutError):
        print('Error with TCP connection ocurred')
        sys.exit(1)
        
    print(clientsocket.recv(1024).decode())
    
    print("You have: 10 attempts.\nEnter a guess containing any 4 of the following: R, B, G, O, Y, P")
    guess = input(" -> ")
    while guess.strip() != 'bye':
        clientsocket.send(guess.encode())
        response = clientsocket.recv(1024).decode()
        print(response)
        start = clientsocket.recv(1024).decode()
        print(start)
        guess = input(" -> ")
    clientsocket.close()

if __name__ == "__main__":
    client()