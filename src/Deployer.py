
''' 
ICLR ROCKETPY - DEPLOYER
Maintained by Raihaan Usman and Krish Nair

Designed to take a converged rocket design through the manufacturing process

- Tool to help engineers define the manufacturing plan + draft an assembly guide
- Task assignment inspired by the 'Responsible (group!) of engineers' philosophy
- Dynamic Gannt chart to handle project timelines and track bottlenecks
- Maintains the dynamic Bill of Materials created in Parts Designer
- Tool tracker to ensure no overlapped plans of work

Planned Integrations
- Teams & Excel via Power Apps / Power Automate
- Valispace (for documentation - or Overleaf lol)

'''

import pickle
import libraries.toolbox as toolbox
# import libraries.components.Component as Component
# import libraries.interfaces.Interface as Interface


# Load rocket object
rocket_name = input("\nEnter the name of your rocket: ")
rocket = toolbox.rocket_load(rocket_name)

