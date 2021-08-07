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



Mission Analyser
****************

- Integrate the ThrustCurve API - https://www.thrustcurve.org/info/api.html - looks easy enough
- Also make generic Engine class for custom definitions



Parts Designer
**************

- STEP exports from F360 - save to Rocket class on request? Will be saving parametric quantities anyway but for complete vehicle reconstruction, may need to record component-level design histories? Seems excessive. Remember that F360 is an official RocketPy dependency, at least for release 1.0.0, so does this matter if all leads/engineers have write access (via cloud - version control is assumed robust) to the vehicle CAD? Probably not.
- 



Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

Lead Developer: Raihaan Usman: raihaan.usman@gmail.com

Developers:

Luis Marques: lfsm01@hotmail.com

Krish Nair: krish.nair19@imperial.ac.uk

