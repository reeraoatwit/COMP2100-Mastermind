# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 16:03:45 2021

"""

import socket
import sys



def client():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = socket.gethostname() # Update before each use if on different hosts
    PORT = 9999
    try:
        clientsocket.connect((HOST, PORT))
    except (InterruptedError, TimeoutError):
        print('Error with TCP connection ocurred')
        sys.exit(1)

    print("You have: 10 attempts left.\nEnter a guess containing any 4 of the following: R, B, G, O, Y, P")
    guess = input(" -> ")
    response = ""
    while guess.strip() != 'bye':
        clientsocket.send(guess.encode()) # Send guess string to be analyzed by server
        response = clientsocket.recv(1024).decode() # print response from mastermind
        if(not response):
            break
        elif (response.endswith("!")): # If pattern guessed correctly, or out of moves, end game
            print(response)
            break
        print(response)
        guess = input(" -> ")
    clientsocket.close()
    sys.exit(0)

if __name__ == "__main__":
    client()