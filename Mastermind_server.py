# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 16:04:21 2021

"""

import socket
import random

def mastermind(socket):
    tcpconnsocket = socket
    answer = ""
    tested = [False,False,False,False]
    validletters = ['R', 'B', 'G', 'O', 'Y', 'P']
        
    for k in range(4): # Generate random string of colored pegs
        rand = random.randint(0,5)
        if(rand == 0): answer += validletters[0]
        elif(rand == 1): answer += validletters[1]
        elif(rand == 2): answer += validletters[2]
        elif(rand == 3): answer += validletters[3]
        elif(rand == 4): answer += validletters[4]
        elif(rand == 5): answer += validletters[5]

        
    guess = tcpconnsocket.recv(1024).decode()
    if not guess:
        return  
    print("from connected user: " + guess)
        
    attempts = 10
    while(attempts > 1):
        for i in range(4):
            tested[i] = False
            
        guess = guess.strip().upper()
        response = ["", "", "", ""]
            
        invalid = False
        
        if(len(guess) != 4):
            invalid = True
        else:
            for i in range(4): # Checks if all the characters in guess are valid, if not, then it restarts the turn
                if(not (guess[i] in validletters)):
                    invalid = True
            
        if(invalid):
            tcpconnsocket.send(("Invalid response, try again").encode())
            guess = tcpconnsocket.recv(1024).decode()
            attempts += 1
            continue
                
        for j in range(4): # Calculates response peg colors based on correctness of guess
            if(guess[j] == answer[j] and tested[j] == False):
                response[j] = "B" # Black if right color and right place
                tested[j] = True
            elif(guess[j] in answer and tested[j] == False):
                if(j>0):
                    for i in range(j):
                        if(guess[i] == guess[j] and tested[i]):
                            response[j] = ""
                else:
                    if(answer.index(guess[j]) > 0):
                        response[j] = ""
                if(response[j] != ""):
                    response[j] = "W"
                tested[j] = True
            else:
                response[j] = "" # X if wrong color
                tested[j] = True
        
        response = shuffle("".join(response))
        
        attempts -= 1
        if(response == "BBBB"):
            response += "\nCongratulations, you guessed the pattern\nGoodbye!"
        else:
            response += " You have: " + str(attempts) + " attempts left.\nEnter a guess containing any 4 of the following: R, B, G, O, Y, P"
            
        tcpconnsocket.send(response.encode())
        if(response.endswith("!")):
            break
        
        guess = tcpconnsocket.recv(1024).decode()
    
    if(attempts == 0):
        tcpconnsocket.send(("\nYou have used up all your attempts. Answer: " + answer + " " + "\nGoodbye!").encode())

def server():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = ''
    PORT = 9999
    serversocket.bind((HOST, PORT))
    serversocket.listen(10)
    while True:
        tcpconnsocket, address = serversocket.accept()
        print("Connection from: " + str(address))
        mastermind(tcpconnsocket) # Start game with client
        tcpconnsocket.close() # Once mastermind() ends game and returns, close tcp connection
    serversocket.close()
            
def shuffle(s): # Shuffles characters around in a string
    result = "".join(random.sample(s, len(s)))
    return result

if __name__ == "__main__":
    server()