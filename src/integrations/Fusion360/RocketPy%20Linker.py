#Author-ICLR
#Description-Linker to RocketPy Core

import adsk.core, adsk.fusion, adsk.cam, traceback, socket

HOST = '127.0.0.1'
PORT = 4200

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        ui.messageBox('RocketPy Linker is running!')

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(b'Hello, world')
            data = s.recv(1024)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def stop(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        ui.messageBox('Terminating RocketPy Linker')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
