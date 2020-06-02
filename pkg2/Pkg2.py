#!/usr/bin/env python

# Standard Lib imports
import sys
sys.path.append("..")

# Local imports
from pkg1 import Pkg1

class Pkg2:
    def __init__(self, name):
        print("#"*20)
        print("pyPackageTest: pkg2")
        print("#"*20)
        self.name = name
        print(self.name)

    def change_name(self, new_name):
        self.name = new_name
        p1inp2 = Pkg1("p1 in p2")
        return p1inp2