#!/usr/bin/env python

class Pkg1:
    def __init__(self, name):
        print("#"*20)
        print("pyPackageTest: pkg1")
        print("#"*20)
        self.name = name
        print(self.name)

    def change_name(self, new_name):
        self.name = new_name