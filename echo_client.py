#!/usr/bin/env python3

from _thread import *
import threading
import sys
import socket
import errno
from socket import error as socket_error

def initConnection(host, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    
    try:
        while True:
            message = input("Enter a message: ")

            sock.sendall(message.encode())

            data = sock.recv(1024)
            print("Received from server: \"",data.decode(),"\"\n")
    
    except EOFError: # Ctrl + D
        print("\n\nExiting")
    except KeyboardInterrupt: #Ctrl + C
        print("\n\nCaught keyboard interrupt. Exiting")
    finally:
        sock.close()

if __name__ == "__main__":
    try:
        host, port = "", 0

        if sys.argv[1] ==  "local":
            host, port = "127.0.0.1", 65432
        elif len(sys.argv) == 3:
            # * Caso host e porta foram especificados
            host, port = sys.argv[1], int(sys.argv[2])

        initConnection(host, port)

    except IndexError:
        print("usage:", sys.argv[0], "<host> <port>")
        print("\tor", sys.argv[0], "local -- to run with predefined host and port")

    except socket_error as serr: # Exceção para tentativa de conexão ao host com porta fechada no lado do servidor 
        if serr.errno != errno.ECONNREFUSED:
            raise serr
        print("Connection refused. Port is perhaps closed on the server side.")