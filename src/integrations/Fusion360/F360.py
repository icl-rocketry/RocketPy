# F360 server class definition
# Maintained by Raihaan Usman and Luis Marques

import socket                                                                       # Socket API for client-server style Inter-Process Communication (IPC)


class F360Server:
    def __init__(self):
        HOST = '127.0.0.1'                                                          # Standard loopback interface address (or just localhost)
        PORT = 4200                                                                 # Luis' idea...

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:                # Creates socket object using IPv4 address family and TCP socket type
            s.bind((HOST, PORT))                                                    # Binds socket with network interface (HOST) and PORT
            s.listen()                                                              # Listens for RPyLinker connection requests
            conn, addr = s.accept()                                                 # accept() blocks and waits for incoming connection - returns tuple of (HOST, PORT)
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    
                    conn.sendall(data)
