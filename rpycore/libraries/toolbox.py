# A bunch of helpful functions!
# Maintained by Raihaan Usman and Luis Marques

import pickle


def flatten_2Darray(array):
    return [item for j in array for item in j]


def rocket_load(name, path="./rockets/"):
    try:
        return(pickle.load(open(path+name+"/"+name+".rpy", "rb")))
    except FileNotFoundError:
        print("\nERROR: RPy file not found")
        exit()