
''' 
ICLR ROCKETPY - DEPLOYER
Maintained by Raihaan Usman and Krish Nair

Designed to take a converged rocket design through the manufacturing process

- Manufacturing Planner to help define the manufacturing plan + draft an assembly guide
- Task Assigner inspired by the 'Responsible (group!) of engineers' philosophy
- Dynamic Gannt chart to handle project timelines and track bottlenecks
- Tool Tracker to ensure no overlapped plans of work

Planned Integrations
- Teams & Excel via Power Apps / Power Automate
- Valispace (for documentation - or Overleaf lol)


-------------
DOCUMENTATION
-------------

Manufacturing Planner

1. For each Component:
    (a) Select/define the process(es) (i.e. roadmap from raw to final state)
    (b) Define target duration, priority and complexity
    (c) Save details to Component within Rocket object

2. For each Interface:
    (a) Select/define integration process(es) (i.e. roadmap from raw to final state)
    (b) Define target duration, priority and complexity
    (c) Save details to Interface within Rocket object

3. Select the engineering group responsible for each component and interface - Task Assigner

4. Order the integration tasks (i.e. for each interface) to create the assembly guide!



Dynamic Gannt chart / Calendar

1. Order the Component manufacturing tasks by priority
2. Order the Assembly/Integration tasks as defined in the Assembly guide
3. For each task, check the Group.availability attribute to calculate the best provisional slots for the duration defined
4. Update the calendars of all engineers + the overall vehicle timeline
5. With the Gannt chart integration, update the Gannt chart
6. Allow the respective engineers to adjust their own tasks manually (timing + room) and to effectively 'pin' them
7. Re-run the above to reshuffle all floating tasks to avoid hardware conflicts, room occupancy, etc.



-----------------------------
TO-DO

Manufacting Planner:
- Modify Rocket, Component and Interface classes to store the manufacturing plans
- Make the Engineer() and Group() classes and library - implements name, year, familiar tools, experience, availability (individual + combined)
- Make a Tool() class - implements name, usage notes
- Make a Process() class and library - implements name, description, hardware + room dependencies, complexity
- Code the CLI boilerplate for Deployer.py


Dynamic Gannt chart:
- Integrate Microsoft Calendar
- Integrate with Excel/Teams/Power Apps/etc
- Make a Room() class and library - implements number, building, address, max. occupancy, Tools dictionary (Tool:Quantity)


-----------------------------
'''

import pickle
import libraries.toolbox as toolbox
# import libraries.components.Component as Component
# import libraries.interfaces.Interface as Interface


# Load rocket object
rocket_name = input("\nEnter the name of your rocket: ")
rocket = toolbox.rocket_load(rocket_name)
