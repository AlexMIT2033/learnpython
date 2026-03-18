# ============================================================
# Lesson 9: Partial functions
# ============================================================
#
# functools.partial lets you "freeze" some arguments of a function, making a new
# function with fewer arguments.
#
#   from functools import partial
#   def add(a, b): return a + b
#   add_ten = partial(add, 10)
#   add_ten(3)   -> 13
#
#   def greet(greeting, name): return greeting + ", " + name
#   say_hi = partial(greet, "Hi")
#   say_hi("Alex")   -> "Hi, Alex"
#
# ----- YOUR TASKS -----
#
# 1. Import partial from functools. Define def multiply(a, b): return a * b.
#    Create double = partial(multiply, 2). Call double(7) and double(11); print both.
# 2. Define def power(base, exp): return base ** exp. Create square = partial(power, exp=2)
#    and cube = partial(power, exp=3). Call square(5) and cube(5); print both.
# 3. Create a function that takes three arguments (e.g. a, b, c) and returns their sum.
#    Use partial to create a new function that fixes the first argument to 1. Call the new
#    function with two numbers and print the result.

from functools import partial

def multiply(a, b): 
    return a * b

double = partial(multiply, 2)
print(double(7))
print(double(11))

def power(base, exp): 
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)
print(square(5))
print(cube(5))

def threesum(a, b, c):
    return a + b + c

task3 = partial(threesum, 1)
print(task3(11, 23))