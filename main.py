#!/usr/bin/env python

from pkg1 import Pkg1
from pkg2 import Pkg2

p1 = Pkg1("p1 init name")
p2 = Pkg2("p2 init name")

p2.change_name("change")

print("#"*20)
print("pyPackageTest: main")
print("#"*20)

