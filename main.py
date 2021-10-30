# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 19:28:53 2021

@author: caseyr3
"""

import random
import sys

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

def main():
    answer = []
    for k in range(4):
        rand = random.randint(0,5)
        if(rand == 0): answer.append(Peg("red", "R", False))
        elif(rand == 1): answer.append(Peg("blue", "B", False))
        elif(rand == 2): answer.append(Peg("green", "G", False))
        elif(rand == 3): answer.append(Peg("orange", "O", False))
        elif(rand == 4): answer.append(Peg("yellow", "Y", False))
        elif(rand == 5): answer.append(Peg("pink", "P", False))
    
    
    attempts = 10
    for k in range(10):
        print("You have: " + str(attempts) + "left.\nEnter a guess containing any 4 of the following: R, B, G, O, Y, P")
        guess = input()
        guess = guess.strip()
        response = ""
        for j in range(4):
            if(guess.index(answer[j].getID()) >= 0 and not(guess[j] == answer[j].getID()) and not(answer[j].getTest())):
                response += "W"
                answer[j].setTest(True)
            elif(guess[j] == answer[j].getID() and not(answer[j].getTest())):
                response += "B"
                answer[j].setTest(True)
                
        print(shuffle(response))
        attempts -= 1
        if(response == "BBBB"):
            print("Congratulations, you guessed the pattern")
            sys.exit()
        elif(attempts == 0):
            print("You have used up all your attemots.")
            sys.exit()
            
def shuffle(s):
    chars = ""
    for c in s:
        chars += c
    return chars

main()