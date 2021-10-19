# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 16:03:45 2021

"""

import socket
import sys

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '' # Update before each use
PORT = 9999

try:
    clientsocket.connect((HOST, PORT))
except (InterruptedError, TimeoutError):
    print('Error with TCP connection ocurred')
    sys.exit(1)

