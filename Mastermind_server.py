# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 16:04:21 2021

"""

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = ''
PORT = 9999

serversocket.bind((HOST, PORT))
serversocket.listen(10)

while True:
    tcpconnsocket, address = serversocket.accept()
    
serversocket.close()