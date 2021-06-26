# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 22:58:45 2020

@author: Raihaan
"""
import valispace
import os

# EDIT PARAMETERS FROM HERE
project_name = 'Sporadic_Impulse_COTS2020'
git = 'The_Sporadic_Impulse.rkt'
git_user = "raihaan123"
v_user = "raihaan.usman19"
repo = "ValiRocket"
# TO HERE


# NO EDITING!!!!!!!!!!!

# Credentials are a secure GitHub secret - reset in your repo
passwd = os.getenv('VSP')
token = os.getenv('TOKEN')

# Start Valispace connection
print("Connecting to Valispace...")
vs = valispace.API(url='iclrocketry.valispace.com',
                        username=v_user, password=passwd)
print("Connected!")

project_id = vs.get_project_by_name(name=project_name)[0]['id']
root = 0
textvali_id = 0


def textvali_next():
    global textvali_id

    if textvali_id == 0:
        projects = vs.get('textvalis/?project=38')
        textvali_id = [x['id'] for x in projects if x['name']][0]
    else:
        textvali_id += 1

    return textvali_id
