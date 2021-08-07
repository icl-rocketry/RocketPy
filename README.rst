========
RocketPy
========


.. image:: https://img.shields.io/pypi/v/rpycore.svg
        :target: https://pypi.python.org/pypi/rpycore

.. image:: https://readthedocs.org/projects/rpycore/badge/?version=latest
        :target: https://rpycore.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status


A rocket maker.


* Free software: MIT license
* Documentation: https://rpycore.readthedocs.io/en/main.



Release 1.0.0 - Main Deliverables
---------------------------------

- Web-based control panel for RocketPy - hosted on Heroku PaaS servers - connected to `rpycore` (PyPI package) for native integrations
- Members securely login with GitHub OAuth and gain access rights as defined by their assigned ICLR role
- Anyone can create personal sandbox environments or collaborate on a shared project - OneDrive is the main data store
- In an RPy environment, there exists a `World` object defining the simulation parameters, a `Rocket` object defining the vehicle entirely and several `Sim` objects, each defining varying mission parameters
- Mission Analyser, Parts Designer and Deployer - RPy's three core applications - are seamlessly integrated into one workflow

        - Mission Analyser - to clearly define top level requirements for the vehicle and dynamically calculate numerical constraints
        - Parts Designer - to seamlessly integrate with F360 to simplify designing components and interfaces by enforcing *in real-time* the vehicle constraints
        - Deployer - to bridge the gap between final design and manufacturing, with intelligent task management and resource allocation



Credits
-------

Development Lead
****************
Raihaan Usman: raihaan.usman@gmail.com

Contributors
************
Luis Marques: lfsm01@hotmail.com, 
Krish Nair: krish.nair19@imperial.ac.uk
