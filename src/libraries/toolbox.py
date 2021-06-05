# A helpful bunch of functions!

import pickle


def flatten_2Darray(array):
    return [item for j in array for item in j]


def rocket_load(name, path="./rockets/"):
    return(pickle.load(open(path+name+".rpy", "rb")))