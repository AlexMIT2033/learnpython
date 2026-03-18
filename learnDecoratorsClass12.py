# ============================================================
# Lesson 11: Decorators
# ============================================================
#
# A decorator is a function that takes another function and returns a new function,
# usually adding some behavior. Syntax: @decorator above the function.
#
#   def my_decorator(func):
#       def wrapper():
#           print("Before")
#           func()
#           print("After")
#       return wrapper
#
#   @my_decorator
#   def say_hello():
#       print("Hello!")
#
#   say_hello()   -> prints Before, Hello!, After
#
# For functions with arguments, use *args, **kwargs in wrapper and pass them to func(*args, **kwargs).
#
# ----- YOUR TASKS -----
#
# 1. Write a decorator log_calls that prints "Calling <function name>" before each call, then
#    calls the function. Use it on a small function (e.g. def add(a,b): return a+b). Call add(1,2)
#    and confirm you see "Calling add" (or similar) then the result.
# 2. Write a decorator that runs the function twice and prints both results. Decorate a function
#    that returns a random number (import random; return random.randint(1,10)). Call it and see two numbers.
# 3. Write a decorator that prints "Start", runs the function, prints "End", and returns the result.
#    Decorate a function that returns "middle" and call it; print the return value.


def log_calls(func):
    def wrapper(*args, **kwargs):
        print("Calling %s" %  func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log_calls
def add(a, b): 
    return a + b

add(1, 2)


def run_multi(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))
        print(func(*args, **kwargs))
        return
    return wrapper
import random

@run_multi
def print_number():
    return random.randint(1, 10)
 
print_number()

def printer(func):
    def wrapper(*args, **kwargs):
        print("Start")
        print(func(*args, **kwargs))
        print("End")
        return
    return wrapper

@printer
def middle():
    return "Middle" 

middle()