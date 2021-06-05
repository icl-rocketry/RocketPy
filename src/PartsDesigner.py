
''' 
ICLR ROCKETPY - PARTS DESIGNER
Maintained by Raihaan Usman and Luis Marques

- Framework for rocket parts design in Fusion 360, handling realtime integration
- Enforces design rules with Valispace integration
- Creates a TCP server and interfaces with the Fusion 360 linker add-in (client)

'''

import pickle
import socket                                                               # Socket API for client-server style Inter-Process Communication (IPC)
import libraries.components.component as component
import libraries.interfaces.interface as interface
import libraries.toolbox as toolbox

# HOST = '127.0.0.1'                                                          # Standard loopback interface address (or just localhost)
# PORT = 4200                                                                 # Luis' idea...

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:                # Creates socket object using IPv4 address family and TCP socket type
#     s.bind((HOST, PORT))                                                    # Binds socket with network interface (HOST) and PORT
#     s.listen()                                                              # Listens for RPyLinker connection requests
#     conn, addr = s.accept()                                                 # accept() blocks and waits for incoming connection - returns tuple of (HOST, PORT)
#     with conn:
#         print('Connected by', addr)
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
            
#             conn.sendall(data)


# Load rocket
rocket_name = input("\nEnter the name of your rocket: ")
rocket = toolbox.rocket_load(rocket_name)


while True:
    print("\n1. Component: Create (C) / Modify (M) / Delete (D)\n\
                2. Interface: Create (C) / Modify (M) / Delete (D)\n\
                3. Exit (E)")
    
    opt = input("Enter choice (e.g. C 1; M 1; D 2; E): ").upper()
    

    if opt == "C 1":
        comp_name = input("\nEnter component name: ")
        comp = component(comp_name)
        
        rocket.add_component(comp)
        print(rocket.components)
        
    elif opt == "M 1":
        
        rocket.show_components()
        comp_id = int(input("\nSelect the component you want to edit: "))
        
        # open fusion on that component 

    if opt == "D 1":
    
    if opt == "C 2":
    
    if opt == "M 2":

    if opt == "D 2":

    if opt == "E":
        break
    
    else:
        continue

    


