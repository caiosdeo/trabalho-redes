#!/usr/bin/env python3

from _thread import *
import threading
import sys
import socket
import errno
from socket import error as socket_error

print_lock = threading.Lock()

def threaded(conn, addr):
    while True:

        data = conn.recv(1024)
        
        decoded = data.decode()
        command = decoded.split(" ")[0]
        arguments = ' '.join([str(substr) for substr in decoded.split(" ")[1:]]).strip()

        print(f"decoded:{decoded}\t command:{command}\t message:\"{arguments}\"")

        if not data or command == "quit":
            # lock released on exit
            print_lock.release()
            print("Connection closed by", addr)
            break

        elif command == "echo":
            if arguments == "":
                arguments = " "
            print("Echoing \'",arguments,"\' to", addr)
            conn.sendall(arguments.encode())

        else:
            conn.sendall("Command not found.".encode())

    conn.close()

def startServer(host, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen()
    print("Listening on", (host, port))
    
    try:
        while True:
            conn, addr = sock.accept()

            print_lock.acquire()
            print("Accepted connection from", addr)

            start_new_thread(threaded, (conn, addr))

    except KeyboardInterrupt:
        print("Caught keyboard interrupt. Exiting")
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

        startServer(host, port)

    except IndexError:
        print("usage:", sys.argv[0], "<host> <port>")
        print("\tor", sys.argv[0], "local -- to run with predefined host and port")

    except socket_error as serr: # Exceção para tentativa de conexão ao host com porta já sendo usados 
        if serr.errno != errno.EADDRINUSE:
            raise serr
        print("Address in use at the moment. Try again later.")

    except Exception as ex:
        print("Exception on startServer", ex)