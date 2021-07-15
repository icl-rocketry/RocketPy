
''' 
ICLR RocketPy - PARTS DESIGNER
Maintained by Raihaan Usman and Luis Marques

- Framework for managing component-level design in Autodesk Fusion 360
- Handles Component and Interface objects
- Enforces design rules with Valispace integration
- Creates an F360Server object to interface with the Fusion 360 RPyLinker add-in (client)
- Maintains the dynamic Bill of Materials

-------------
DOCUMENTATION
-------------

Bill of Materials

1. Create excel workbook containing:
    -Components as worksheets 
    -Sub-components as rows
    -Sub-component Material, Volume, Weight, Quantity, Unit Cost, Total Cost, Reference as columns
    -TOTAL OVERALL COST of a Component by adding Total Cost of each sub-component

2. Edit a previously created BoM workbook at will

3. Save workbook in the specific directory

4. BoM workbook data can be accessed by Microsoft PowerApp and displayed for user

5. [ Database of Sub-component objects can be created and later manipulated and then re-converted into Excel format ] ~Idea?







-----
TO-DO
-----

Bill of Materials:
-Convert workbook creation+manipulation code into user-friendly streamlit
-Demonstrate Microsoft PowerApp integration with the Excel Bill of Materials workbook
-[ Create a class for Sub-component ] ~Idea?


'''

import pickle
import libraries.components.Component as Component
import libraries.interfaces.Interface as Interface
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
        rocket.create_component(input("\nEnter component name: "))
        rocket.show_components()
        
    elif opt == "M 1":
        
        rocket.show_components()
        comp_id = int(input("\nSelect the component you want to edit: "))
        
        # Launch Fusion 360 for specified component
        continue

    # if opt == "D 1":
    
    # if opt == "C 2":
    
    # if opt == "M 2":

    # if opt == "D 2":

    elif opt == "E":
        break


    


