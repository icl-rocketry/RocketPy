# Parts Designer tool
# Opens a TCP server and interfaces with the Fusion 360 linker

import socket

HOST = '127.0.0.1'
PORT = 42000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            
            conn.sendall(data)