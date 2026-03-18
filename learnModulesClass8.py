# ============================================================
# Lesson 2: Modules and Packages
# ============================================================
#
# A MODULE is a .py file. You can use code from another file by importing.
#
#   import math
#   math.sqrt(16)   -> 4.0
#
#   from math import sqrt, pi
#   sqrt(16)
#   print(pi)
#
#   from math import *   (imports everything; usually avoid)
#
#   import myfile as m
#   m.my_function()
#
# A PACKAGE is a folder containing an __init__.py (can be empty) and other
# .py files or subpackages. Then you can:
#
#   import mypackage
#   from mypackage import something
#   from mypackage.submodule import something
#
# ----- YOUR TASKS -----
#
# 1. Create a file mymath.py in this folder. In it, define a function add(a, b)
#    that returns a + b, and a variable TAU = 6.28. Save the file.
# 2. In this file (learnModules.py), add at the top: import mymath. Then call
#    mymath.add(3, 5) and print the result. Print mymath.TAU.
# 3. Use "from mymath import add, TAU". Call add(10, 20) and print TAU.
# 4. Create a folder named mypackage. Inside it, create __init__.py (can be
#    empty) and helper.py. In helper.py define def greet(name): return "Hi, " + name.
# 5. Here, write: from mypackage.helper import greet. Call greet("Alex") and print the result.

import mymath
print(mymath.add(3, 5))
print(mymath.TAU)

from mymath import add, TAU
print(add(10, 20))
print(TAU)

from mypackage.helper import greet
print(greet("Alex"))