
''' 
ICLR RocketPy - MISSION PLANNER
Maintained by Raihaan Usman and Luis Marques

- Systems engineers describe high-level objectives and requirements
- MISSION PLANNER calculates and enforces constraints from mission requirements

There are several high-level "Rocket Objective" targets which set the 'enforced constraints' vector
E.g. Payload --> Mass, Dimensions, Flight objective, Class
     Staging --> Number of Stages, Flight objective, Class


'Defined Constraints' output vector: by default empty; 
'''

import pickle                                                                                           # For serialise/deserialise
import libraries.rockets.Rocket as Rocket                                                               # Rocket base class
import libraries.toolbox as toolbox                                                                     # Helper functions             
import libraries.systems.Constraint as Constraint                                                       # Constraints base class


# List of all design constraints - remember these are ranges, not necessarily exact values
constraints = [ ["apogee", "flight_time", "max_velocity"],                                              # Flight Constraints
                ["radial_drift", "safety_factor", "ground_hit_velocity"],                               # Safety Constraints
                ["class", "cost"],                                                                      # Team Limitations
                ["payload_mass", "payload_volume"],                                                     # Payload Requirements
                ["num_stages"],                                                                         # Staging Requirements
                ["num_motors", "isp", "burn_time", "thrust_limits"]                                     # Engine Requirements
              ]

constraints_flat = toolbox.flatten_2Darray(constraints)

rocket_objectives = {"Payload": [1,3], "Staging": [1,4], "Novel Propulsion": [1,5], "Custom": []}       # Top-level objectives

defined_constraints = {}

# Select new or existing rocket design
while True:

    opt = int(input("Select 1 to create a new rocket, 2 to load an existing design: "))

    if opt == 1:
        name = input("\nEnter the name of your new rocket: ")
        print("")
        [print(f"{i}. {n}") for i,n in enumerate(rocket_objectives)]
        objectives_opt = int(input("Select your rocket objective: "))

        # Highlights mandatory fields
        enforced_constraints = [constraints[i] for i in rocket_objectives[list(rocket_objectives)[objectives_opt]]]
        enforced_constraints = toolbox.flatten_2Darray(enforced_constraints)
        break
        
    elif opt == 2:
        name = input("\nEnter the name of your rocket: ")
        rocket = toolbox.rocket_load(name)

        # Retrieving data from Rocket object
        enforced_constraints = rocket.enf_const
        defined_constraints = rocket.constraints

        break
        
    
while True:

    print("")
    count = 0                                                                                           
    for const in constraints_flat:
        if const in enforced_constraints:
            try: print(f"{count}. (REQUIRED) {const}: {defined_constraints[const]}")                    
            except: print(f"{count}. (REQUIRED) {const}")
        else: 
            try: print(f"{count}. {const}: {defined_constraints[const]}")
            except: print(f"{count}. {const}")
        count +=1

    user_const = input("\nUsing SI units, set a constraint (idx lower_bound upper_bound) or type \"done\" to proceed: ")
    
    if (user_const.lower()) == "done":
        
        if all(const in defined_constraints for const in enforced_constraints):
            rocket = Rocket.Rocket(name, defined_constraints, enforced_constraints)
            # rocket = systems.calculate(rocket)

            rocket.save()
            break

        else:
            print("\nPlease define all required constraints before saving\n")
            continue

    user_const = user_const.split()

    try:
        if (float(user_const[1]) > float(user_const[2]) or float(user_const[1]) < 0 or float(user_const[2]) < 0):
            print("\nERROR: Ensure the lower bound is smaller than the upper bound and that both values are +ve.")
            continue
    except:
        print("\nERROR: Illegal input. Try again")
        continue

    defined_constraints[constraints_flat[int(user_const[0])]] = [float(user_const[1]), float(user_const[2])]

print("\nDefined rocket constraints:\n" + str(rocket.constraints) + f"\nSaved final model in rockets/{name}/{name}.rpy.")