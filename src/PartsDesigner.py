
''' 
ICLR ROCKETPY - PARTS DESIGNER
Maintained by Raihaan Usman and Luis Marques

- Framework for rocket parts design in Fusion 360, handling realtime integration
- Handles Component and Interface objects
- Enforces design rules with Valispace integration
- Creates a TCP server and interfaces with the Fusion 360 linker add-in (client)

'''

import pickle
import libraries.components.component as component
import libraries.interfaces.interface as interface
import libraries.toolbox as toolbox



# Load rocket object
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
        print(rocket.show_components())
        
    elif opt == "M 1":
        
        rocket.show_components()
        comp_id = int(input("\nSelect the component you want to edit: "))
        
        # Launch Fusion 360 for specified component
        continue

    if opt == "D 1":
    
    if opt == "C 2":
    
    if opt == "M 2":

    if opt == "D 2":

    if opt == "E":
        break
    
    else:
        continue

    


