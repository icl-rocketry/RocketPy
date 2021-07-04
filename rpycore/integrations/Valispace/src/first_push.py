# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 15:40:09 2021

@author: Raihaan
"""
from globalV import root, git
from classes import component, vali, textvali
from lxml import objectify
import pickle


# First push function
def fpush():
    global git

    # Loading RKT file
    with open(git) as f:
        git = f.read()

    # Generating root object with lxml + resetting head
    full_root = objectify.fromstring(git)
    root = full_root.DesignInformation.RocketDesign

    # Adjusting the names to meet Valispace API requirement
    for components in root.iter('Name'):
        components._setText(components.text.replace(" ", "_"))

    # Creating a rocket component object and pushing to Valispace
    rocket = component(root.Name.text, "null")

    # Useful attributes for marking changes
    root.Name.set("id", str(rocket.id))

    # Making a nice tree iterator and calling the parser function
    iterator = root.iterchildren()
    parser(iterator, rocket)

    # Finally saving the latest parsed RKT file as 'parsed.rocket'
    with open("parsed.rocket", "wb") as f:
        pickle.dump(full_root, f)


# Probably the most annoying bit...
def parser(iterator, parent):
    # global root
    this_level = [*iterator]

    # Selects all vali elements & pushes, returns vali type objects
    vali_elems = [x for x in this_level if isinstance(x.text, (str, int, float)) and x != '']
    print(vali_elems)
    vali_objs = [vali_pusher(vali_elem, parent) for vali_elem in vali_elems]
    print(vali_objs)

    # Assigning attributes the tree vali elements - useful for lookups
    [vali_elem.set("id", str(vali_obj.id)) for vali_elem, vali_obj in zip(vali_elems, vali_objs)]

    # Selects all next level components in a list of object iterators
    next_level = [comp for comp in this_level if (not isinstance(comp.text, (str, int, float)) and comp != '' and comp.tag != 'AttachedParts')]

    # Handling attached components in 'inner' array
    inner = [comp.iterchildren() for comp in this_level if comp.tag == 'AttachedParts']
    inner = [i for x in inner for i in x]

    if len(inner) > 0:
        next_level.extend(inner)

    # Iterating over each attached subcomponent + pushing
    comp_objs = [component_pusher(comp_elem, parent) for comp_elem in next_level]

    # Assigning attributes the tree component elements - useful for lookups
    [comp_elem.set("id", str(comp_obj.id)) for comp_elem, comp_obj in zip(next_level, comp_objs)]

    # Step down one level - note the self call
    [parser(comp_elem.iterchildren(), comp_obj) for comp_elem, comp_obj in zip(next_level, comp_objs)]


def vali_pusher(vali_elem, parent):
    # print(vali.tag+" = "+vali.text+" <- "+str(parent.id))
    try:
        newVali = vali(str(vali_elem.tag), parent, str(vali_elem.text))
    except Exception:
        newVali = textvali(str(vali_elem.tag), parent, str(vali_elem.text))
    except Exception:
        newVali = textvali(str(vali_elem.tag), parent, "Undefined")

    return newVali


def component_pusher(comp, parent):
    try:
        print("Using name")
        name = comp.Name.text
    except Exception:
        print("Using tag")
        name = comp.tag

    print(name, "belongs to", parent.id)

    newComponent = component(str(name), parent)
    return newComponent


# Just for development, remove in production
# fpush()










# # Writing updates to RKT file - works but does not belong here
# with open('The_Sporadic_Impulse_archive.rkt', 'wb') as f:
#     # for i in root.iterdescendants():
#     #     i.attrib.clear()
#     f.write(etree.tostring(full_root, pretty_print=True))



## Stuff that works!

# print(root.DesignInformation.RocketDesign.Name)
# root.DesignInformation.RocketDesign.Name._setText('b')
# root.DesignInformation.RocketDesign.Name.set("id", "12")

# print(root.DesignInformation.RocketDesign.Name)



## For spotting unchanged case - obsolete

# # if git == archive:
# #     print("Rkt file unchanged")
# #     exit()


## Garbage!

# parent = 
# tree = etree.ElementTree(root.DesignInformation.RocketDesign)
# print(isinstance(tree.getroot(), objectify.ObjectifiedElement))

# print(root.DesignInformation.RocketDesign.Name.text)
# print(tree.attrib)

# for appt in root.DesignInformation.RocketDesign.iterchildren():
#     for e in appt.iterchildren():
#         for i,f in enumerate(e.iterchildren()):
#             print("%s --> %s" % (f.tag, f.text))
#             print(i)

# def getChild(root):
#     return([i.getchildren() for i in root])

# for i in range(0,3):
#     print([[k.tag for k in j] for j in getChild(root.getchildren())])
#     root = 




## More garbage!

# print([x for x in git.descendants])
# print(xdif.diff_files(globalV.archive, globalV.git, diff_options={'fast_match': True}))