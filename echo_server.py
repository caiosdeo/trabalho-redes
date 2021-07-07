#!/usr/bin/env python3

from _thread import *
import threading
import sys
import socket

print_lock = threading.Lock() # ? Ainda n sei

def threaded(conn, addr):
    while True:

        data = conn.recv(1024)
        if not data:
            # lock released on exit
            # print_lock.release() # ?
            print("Connection closed with", addr)
            break

        print("Echoing", repr(data), "to", addr)
        conn.sendall(data)

    conn.close()

def startServer(host, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen()
    print("Listening on", (host, port))
    
    try:
        while True:
            conn, addr = sock.accept()

            # ? print_lock.acquire()
            print("Accepted connection from", addr)

            start_new_thread(threaded, (conn, addr))

    except KeyboardInterrupt:
        print("\nCaught keyboard interrupt. Exiting")
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

    except Exception:
        print("usage:", sys.argv[0], "<host> <port>")
        print("\tor", sys.argv[0], "local -- to run with predefined host and port")