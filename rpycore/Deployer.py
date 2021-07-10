
'''
ICLR RocketPy - DEPLOYER
Maintained by Raihaan Usman and Krish Nair

The missing link between your final rocket design and flight!

DEPLOYER brings 5 important capabilities to complete the RocketPy workflow-

    - Manufacturing Planner to standardize manufacturing into unit tasks for each component
    - Assembly Planner to standardize the assembly process for each modular interface
    - Task Assigner inspired by the 'Responsible (group!) of Engineers' philosophy
    - Dynamic Gantt to handle the vehicle production timeline and track bottlenecks
    - Tool Tracker to ensure no overlapping plans of work with the same tool dependency

Planned Integrations
- Teams & Excel via Power Apps / Power Automate
- Valispace (for documentation - or Overleaf lol)


-------------
DOCUMENTATION
-------------

Manufacturing Planner

    1. For each COMPONENT in rocket file:
        (a) Select/define the manufacturing process(es) (i.e. roadmap from raw to final part)
        (b) Define target duration, priority and complexity scores
        (c) Save job details to Component object within Rocket object

    2. For each INTERFACE in rocket file:
        (a) Select/define the integration process(es)
        (b) Define target duration, priority and complexity scores
        (c) Save job details to Interface object within Rocket object

    - Each

Job Assigner
    - Provisionally assign an engineering group responsible for each component and interface (job) based on engineer profile


Assembly Guide
    - Order integration tasks (i.e. fitting each interface) to construct the Assembly Guide!


Dynamic Gantt chart / Calendar

    1. Order component manufacturing tasks by priority
    2. Order integration tasks as prescribed in the Assembly Guide
    3. For each task, check the Group.availability attribute to calculate provisional slots for the defined duration
    4. Update the calendars of all engineers + the overall vehicle timeline
    5. Update Gantt chart (with integration)
    6. Allow respective engineers to adjust their own tasks manually (timing + room) and to 'pin' them
    7. Re-run module to recalculate all floating tasks to avoid hardware conflicts, room occupancy limits, etc.


-----
TO-DO
-----

Manufacting Planner:
- Modify Rocket, Component and Interface classes to store the manufacturing plans
- Write the Engineer() and Group() classes and library - implements name, team, year, familiar Tools, experience, availability (individual + combined)
- Write the Tool() class and library - implements name, usage notes
- Write the Process() class and library - implements name, description, Tool + Room dependencies, complexity
- Write the CLI boilerplate for Deployer.py


Dynamic Gantt chart:
- Integrate Microsoft Calendar
- Integrate with Excel/Teams/Power Apps/etc
- Write the Room() class and library - implements number, building, address, max. occupancy, Tools dictionary (Tool:Quantity)

'''


import pickle
import libraries.toolbox as toolbox
import libraries.processes.Process as Process
import libraries.engineers.Engineer as Engineer
import libraries.engineers.Group as Group
import libraries.tools.Tool as Tool
import libraries.rooms.Room as Room


# Load rocket object
rocket_name = input("\nEnter the name of your rocket: ")
rocket = toolbox.rocket_load(rocket_name)


manufacturing_processes=['Process1','Process2','Process3','Custom','Done']                                              # List of given manufacturing processes + 1 custom process
integration_processes=['Process1','Process2','Process3','Custom','Done']                                                # List of given integration processes + 1 custom process

print("--------Components--------")


for component in rocket.components:

    while True:

        print(f"For component ({component.name}), select a preset manufacturing process, or make custom:")
        print(manufacturing_processes)

        ch = int(input("Choose a process:"))                                                                            # Selecting which process to add to the Component "processes" list

        # The whole "prcoessess" list defines 1 job

        if ch == len(manufacturing_processes) - 1:                                                                      #If it is a Custom Process

            #Specify name:
            name = input("Name this process: ")
            #Specify description:
            desc = input("Add a generic description for this process: ")
            #Specify extra_description:
            extra_desc = input("Add a specific description for this component: ")

            process=Process(name, desc, extra_desc) #Create a process object

            '''
            #Specify tools:
            print("----------Tools----------")
            tools=[]
            while True:
                ch1=int(input("Tool Options: 1.Add tool 2.Delete tool 3.Done"))

                if ch1==1:

                    tool=input("Add tool: ")
                    tools.append(tool)
                elif ch1==2:

                    tool=input("Specify tool to delete: ")
                    if tool not in tools:
                        print("Tool does not exist in list!")
                        continue
                    else:
                        tools.delete(tool)
                else:
                    break
            process.add_tools(tools)

            #Specify room:
            print("----------Room----------") #!!!I've left the room to be specified as a string for now but it has to be an object (Pls change later)!!!
            rooms=[]
            while True:
                ch1=int(input("Room Options: 1.Add room 2.Delete room 3.Done"))

                if ch1==1:

                    room=input("Add room: ")
                    rooms.append(room)
                elif ch1==2:

                    room=input("Specify room to delete: ")
                    if room not in rooms:
                        print("Room does not exist in list!")
                        continue
                    else:
                        rooms.delete(tool)
                else:
                    break
            process.add_rooms(rooms)

            #Specify complexity
            print("----------Complexity----------")
            complexity=input("Enter complexity of the process")    
            process.add_complexity(complexity) #!!!For now I've left it as a simple integer to be specified and not as a fxn of the list of tools complexities (Pls change later)!!!    
        '''
            component.add_process(process)                                                      # Adding to the component job (list)


        elif ch != len(manufacturing_processes):
            manufacturing_processes[ch-1].mod_extra_desc(input(("Add a specific description for this component: ")))
            component.add_process(manufacturing_processes[ch-1])                                                      # Adding to the processess list
        
        else:
            break


    component.target_duration = int(input("Enter target duration (in hours): "))
    component.priority = int(input("Enter priority score: 1. High 2. Medium 3. Low"))
    component.complexity = int(input("Enter complexity score"))


print("--------Interfaces--------")

for interface in rocket.interfaces:

    while True:

        print(f"For interfaces ({interface.name}), select a preset integration process, or make custom:")
        print(integration_processes)

        ch = int(input("Choose a process:"))                                                                            # Selecting which process to add to the Component "processes" list

        # The whole "prcoessess" list defines 1 job

        if ch == len(integration_processes) - 1:
            name = input("Name this process: ")
            desc = input("Add a generic description for this process: ")
            extra_desc = input("Add a specific description for this interface: ")

            #The below was copied from the above component section (IT WILL OBVIOUSLY HAVE TO BE EDITED):
            '''
            #Specify tools:
            print("----------Tools----------")
            tools=[]
            while True:
                ch1=int(input("Tool Options: 1.Add tool 2.Delete tool 3.Done"))

                if ch1==1:

                    tool=input("Add tool: ")
                    tools.append(tool)
                elif ch1==2:

                    tool=input("Specify tool to delete: ")
                    if tool not in tools:
                        print("Tool does not exist in list!")
                        continue
                    else:
                        tools.delete(tool)
                else:
                    break
            process.add_tools(tools)

            #Specify room:
            print("----------Room----------") #!!!I've left the room to be specified as a string for now but it has to be an object (Pls change later)!!!
            rooms=[]
            while True:
                ch1=int(input("Room Options: 1.Add room 2.Delete room 3.Done"))

                if ch1==1:

                    room=input("Add room: ")
                    rooms.append(room)
                elif ch1==2:

                    room=input("Specify room to delete: ")
                    if room not in rooms:
                        print("Room does not exist in list!")
                        continue
                    else:
                        rooms.delete(tool)
                else:
                    break
            process.add_rooms(rooms)

            #Specify complexity
            print("----------Complexity----------")
            complexity=input("Enter complexity of the process")    
            process.add_complexity(complexity) #!!!For now I've left it as a simple integer to be specified and not as a fxn of the list of tools complexities (Pls change later)!!!    
        '''
            interface.add_process(Process(name, desc, extra_desc))                                                      # Adding to the component job (list)

        elif ch != len(integration_processes):
            integration_processes[ch-1].mod_extra_desc(input(("Add a specific description for this interface: ")))
            interface.add_process(integration_processes[ch-1])                                                          # Adding to the processess list
        
        else:
            break


    interface.target_duration = int(input("Enter target duration (in hours): "))
    interface.priority = int(input("Enter priority score: 1. High 2. Medium 3. Low"))
    interface.complexity = int(input("Enter complexity score"))



#Job Assigner
print("x----------Job Assigner----------x")


#Assembly Guide

#Note: I'm assumming we have to ordere the interface processes (given above). I could be stupid, so recheck later

print("x----------Assembly Guide----------x")

tasks_copy=[] #Dummy List that will contain each interface's job
tasks=[]      #ORDERED List of each interface's job

for interface in rocket.interfaces:
    job=interface.job
    tasks_copy.append(job)


print("List of integration tasks:")
print(f"{i+1}. {tasks_copy[i]} "for i in range(len(tasks_copy)-1))

for i in range(len(tasks_copy)-1):
    ch=input(f"Choose task (enter the above corresponding number) for Task {i+1}: ")
    tasks.append(tasks_copy[ch-1])


print("Ordered List of Integration Tasks:")
print(f"{i+1}. {tasks[i]} "for i in range(len(tasks)-1))





