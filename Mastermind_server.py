# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 16:04:21 2021

"""

import socket
import random

class Peg:
    color = ""
    iD = ''
    tested = False
    
    def __init__(self,c,x,t):
        self.color = c
        self.iD = x
        self.tested = t
        
    def getColor(self):
        return self.color

    def getID(self):
        return self.iD
    
    def getTest(self):
        return self.tested
    
    def setTest(self,newT):
        self.tested = newT



def server():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = ''
    PORT = 9999
    serversocket.bind((HOST, PORT))
    serversocket.listen(10)
    while True:
        tcpconnsocket, address = serversocket.accept()
        print("Connection from: " + str(address))
        while True:
            answer = ""
            tested = [False,False,False,False]
            for k in range(4):
                rand = random.randint(0,5)
                if(rand == 0): answer += "R"
                elif(rand == 1): answer += "B"
                elif(rand == 2): answer += "G"
                elif(rand == 3): answer += "O"
                elif(rand == 4): answer += "Y"
                elif(rand == 5): answer += "P"
            
            
            
            tcpconnsocket.send(answer.encode())
            
            guess = (str(tcpconnsocket.recv(1024).decode()))
            if not guess:
                break        
            print("from connected user: " + guess)
            
            attempts = 10
            for k in range(10):
                for i in range(4):
                    tested[i] = False
                
                guess = guess.strip().upper()
                response = ""

                for j in range(4):
                    if(guess[j] == answer[j] and tested[j] == False):
                        response += "B"
                        tested[j] = True
                    elif(guess[j] in answer and tested[j]== False):
                        response += "W"
                        tested[j] = True
                    else:
                        response += "X"
                        tested[j] = True
                        
                tcpconnsocket.send((shuffle(response).encode()))
                
                attempts -= 1
                if(response == "BBBB"):
                    tcpconnsocket.send(("Congratulations, you guessed the pattern").encode())
                    break
                elif(attempts == 0):
                    tcpconnsocket.send(("You have used up all your attempts. Answer: " + answer).encode())
                    break
                tcpconnsocket.send(("You have: " + str(attempts) + " left.\nEnter a guess containing any 4 of the following: R, B, G, O, Y, P").encode())
                guess = (str(tcpconnsocket.recv(1024).decode()))
            tcpconnsocket.close()      
            serversocket.close()
            
def shuffle(s):
    result = "".join(random.sample(s, len(s)))
    return result

if __name__ == "__main__":
    server()