# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 23:54:48 2020

@author: Raihaan
"""


# Component API call class
class component:

    def __init__(self, name, parent):

        from globalV import project_id, project_name

        self.name = str(name)
        self.parent = parent
        self.project_id = project_id
        self.project_name = str(project_name)
        try:
            self.path = self.parent.path+'.'+self.name
            self.parent_id = self.parent.id
        except Exception:
            self.path = self.name
            self.parent_id = "null"

        # Valispace push call
        self.push()

    def push(self):

        from globalV import vs

        vs.post_data(type='component', data="""{
            "name": \"""" + self.name + """\",
            "parent": """ + str(self.parent_id) + """,
            "project": """ + str(self.project_id) + """,
            "tags": [
              9
            ]
        }""")

        self.id = vs.get_component_by_name(unique_name=self.path, 
                            project_name=self.project_name)['id']

        # return(self.id)


# Vali API call class
class vali:

    def __init__(self, name, parent, value):

        self.parent = parent
        self.name = name
        self.value = str(value)
        self.path = self.parent.name+'.'+self.name

        # Valispace push call
        self.push()

    def push(self):

        from globalV import vs, project_name

        data="""{
            "shortname": \"""" + self.name + """\",
            "formula": """ + self.value + """,
            "parent": """ + str(self.parent.id) + """,
            "tags": [
              9
            ]
        }"""
        # print(data)
        # print(self.path)

        vs.post_data(type='vali', data=data)

        self.id = vs.get_vali_by_name(vali_name=self.path, 
                            project_name=project_name)['id']

        # return(self.id)


class textvali:

    def __init__(self, name, parent, text):

        self.parent = parent
        self.name = name
        self.text = text
        self.path = self.parent.name+'.'+self.name

        # Valispace push call
        self.push()

    def push(self):
        # global textvali_id

        from globalV import vs, project_name, textvali_next

        vs.post_data(type='textvali', data="""{
            "shortname": \"""" + self.name + """\",
            "text": \"""" + self.text + """\",
            "parent": """ + str(self.parent.id) + """,
            "tags": [
              9
            ]
        }""")

        # self.id = vs.get_vali_by_name(vali_name=self.path, 
        #                     project_name=project_name)['id']
        self.id = textvali_next()
        print("So basically right: ", self.id)

        # return(self.id)
