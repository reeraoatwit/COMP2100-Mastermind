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
            guess = (str(tcpconnsocket.recv(1024).decode()))
            if not guess:
                break        
            print("from connected user: " + guess)
            answer = []
            for k in range(4):
                rand = random.randint(0,5)
                if(rand == 0): answer.append(Peg("red", "R", False))
                elif(rand == 1): answer.append(Peg("blue", "B", False))
                elif(rand == 2): answer.append(Peg("green", "G", False))
                elif(rand == 3): answer.append(Peg("orange", "O", False))
                elif(rand == 4): answer.append(Peg("yellow", "Y", False))
                elif(rand == 5): answer.append(Peg("pink", "P", False))
            
            attempts = 9
            for k in range(10):
                start = "You have: " + str(attempts) + " left.\nEnter a guess containing any 4 of the following: R, B, G, O, Y, P"
                tcpconnsocket.send(start.encode())
                tcpconnsocket.shutdown(socket.SHUT_WR)
                guess = guess.strip().upper()
                response = ""
                for i in range(4):
                    answer[i].setTest(False)
                for j in range(4):
                    if((answer[j].getID() in guess) and not(guess[j] == answer[j].getID()) and not(answer[j].getTest())):
                        response += "W"
                        answer[j].setTest(True)
                    elif(guess[j] == answer[j].getID() and not(answer[j].getTest())):
                        response += "B"
                        answer[j].setTest(True)
                        
                tcpconnsocket.send((shuffle(response).encode()))
                attempts -= 1
                if(response == "BBBB"):
                    tcpconnsocket.send(("Congratulations, you guessed the pattern").encode())
                    break
                elif(attempts == 0):
                    tcpconnsocket.send(("You have used up all your attemots.").encode())
                    break
                tcpconnsocket.close()      
            serversocket.close()
            
def shuffle(s):
    chars = ""
    for c in s:
        chars += c
    return chars
if __name__ == "__main__":
    server()