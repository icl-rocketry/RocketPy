
''' 
ICLR ROCKETPY - MISSION ANALYSER

- User describes high level requirements
- Program sets and enforces bounds based on mission objectives

There are several "Rocket Focus" targets which pre-populate the output vector
E.g. Payload --> Mass, Dimensions, Flight objective, Class
     Staging --> Number of Stages, Flight objective, Class


Output Vector: by default null; 
'''

import pickle       # For serialise/deserialise
import Rocket       # Rocket class


# Functions
def load(name, path="./rockets/"):
    return(pickle.load(open(path+name+".pickle", "rb")))


# List of all design constraints - remember these are ranges, not necessarily exact values
constraints = [ ["apogee", "flight_time", "ground_hit_velocity", "max_velocity", "radial_drift"],       # Flight Constraints
                ["class", "cost"],                                                                      # Team Limitations
                ["payload_mass", "payload_volume"],                                                     # Payload Characteristics
                ["num_stages"],                                                                         # Staging Requirements
                ["num_motors", "Isp", "burn_time", "thrust_limits"]                                     # Engine Characteristics
              ]

constraints_flat = [item for j in constraints for item in j]

rocket_focus = {"Payload": [2], "Staging": [3], "Custom": []}                                           # Top level objectives

defined_constraints = {}

# Select new or existing rocket design
while True:

    opt = int(input("Select 1 to create a new rocket, 2 to load an existing design: "))

    if opt == 1:
        name = input("\nEnter the name of your new rocket: ")
        print("")
        [print(f"{i}. {n}") for i,n in enumerate(rocket_focus)]
        focus_opt = int(input("Select your rocket focus: "))

        # Highlights mandatory fields
        enforced_constraints = [constraints[i] for i in rocket_focus[list(rocket_focus)[focus_opt]]]
        enforced_constraints = [item for j in enforced_constraints for item in j]

        break
        
    elif opt == 2:
        name = input("\nEnter the name of your rocket: ")
        rocket = load(name)

        # Retrieving data from Rocket object
        enforced_constraints = rocket.enf_const
        defined_constraints = rocket.constraints

        break
        
    
while True:

    print("")
    count = 0                                                                                           # Because we're code noobs apparently
    for const in constraints_flat:
        if const in enforced_constraints:
            try: print(f"{count}. (REQUIRED) {const}: {defined_constraints[const]}")                    # More noob stuff
            except: print(f"{count}. (REQUIRED) {const}")
        else: 
            try: print(f"{count}. {const}: {defined_constraints[const]}")
            except: print(f"{count}. {const}")
        count +=1

    user_const = input("\nUsing SI units, set a constraint (idx lower_bound upper_bound) or type \"done\" to end the script: ")
    
    if (user_const.lower()) == "done":
        
        if all(const in defined_constraints for const in enforced_constraints):
            rocket = Rocket.Rocket(name, defined_constraints, enforced_constraints)
            rocket.save()
            break

        else:
            print("\nBroski more data pls\n")
            continue

    user_const = user_const.split()

    if (float(user_const[1]) > float(user_const[2]) or float(user_const[1]) < 0 or float(user_const[2]) < 0):
        print("\nMake sure the lower bound is smaller than the upper bound and that both values are +ve.")
        continue
    
    # One liner cos we're cool
    defined_constraints[constraints_flat[int(user_const[0])]] = [float(user_const[1]), float(user_const[2])]


# Evaluate design envelopes 
# Very basic, idea is that Systems expands this!


[rocket.add_constraint(i, j) for i, j in zip(["min_impulse", "mass", "wind_lims"])]