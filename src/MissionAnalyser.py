''' MISSION ANALYZER

- User describes high level req.
- Program sets and enforces boundaries based on mission objectives

There are different "Rocket Focus" which pre-populate the output vector
E.g. Payload --> Mass, Dimensions, Flight objective, Class
     Staging --> Number of Stages, Flight objective, Class


Output Vector: by default null; 
'''
import pickle
import Rocket


### Functions ###
def load(name, path="./rockets/"):
    return(pickle.load(open(path+name+".pickle", "rb")))



constraints = [ ["apogee", "flight_time", "ground_hit_velocity", "max_speed", "radial_drift"],          # Flight Constraints
                ["class", "cost"],                                                                      # Team Limitations
                ["payload_mass", "payload_volume"],                                                     # Payload Requirements
                ["number_stages"]
              ]

constraints_flat = [item for j in constraints for item in j]

rocket_focus = {"Payload": [2], "Staging": [3], "Custom": []}

defined_constraints = {}

# Select new or existing rocket design
while True:

    opt = int(input("Select 1 to create a new rocket, 2 for loading an existing one: "))

    if opt == 1:
        name = input("\nEnter the name of your rocket: ")
        print("")
        [print(f"{i}. {n}") for i,n in enumerate(rocket_focus)]
        focus_opt = int(input("Select your rocket focus: "))

        enforced_constraints = [constraints[i] for i in rocket_focus[list(rocket_focus)[focus_opt]]]
        enforced_constraints = [item for j in enforced_constraints for item in j]

        break
        
    elif opt == 2:
        name = input("\nEnter the name of your rocket: ")
        rocket = load(name)

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
    
    user_const = input("\nUsing SI units, set a constraint (idx lower_bound upper_bound) or type \"done\" to end the script: ")
    
    if (user_const.lower()) == "done":
        
        if all(const in defined_constraints for const in enforced_constraints):
            rocket = Rocket.Rocket(name, defined_constraints, enforced_constraints)
            rocket.save()
            break

        else:
            print("\nBroski more data\n")
            continue

    user_const = user_const.split()

    if (float(user_const[1]) > float(user_const[2]) or float(user_const[1]) < 0 or float(user_const[2]) < 0):
        print("\nMake sure the lower bound is smaller than the upper bound and that both values are +ve.")
        continue

    defined_constraints[constraints_flat[int(user_const[0])]] = [float(user_const[1]), float(user_const[2])]





