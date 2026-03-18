# ============================================================
# Lesson 10: Closures
# ============================================================
#
# A closure is a function that "remembers" variables from the scope where it was
# defined (the enclosing function), even after that scope has finished.
#
#   def make_adder(n):
#       def adder(x):
#           return x + n
#       return adder
#
#   add_5 = make_adder(5)
#   add_5(10)   -> 15
#
# The inner function adder "closes over" n. Each call to make_adder creates a
# different adder that remembers its own n.
#
# ----- YOUR TASKS -----
#
# 1. Write make_multiplier(factor). It should return a function that takes one
#    number and returns that number times factor. Create triple = make_multiplier(3),
#    call triple(4) and print the result.
# 2. Write make_greeter(greeting). It should return a function that takes a name
#    and returns greeting + ", " + name + "!". Create say_hi = make_greeter("Hi") and
#    say_hello = make_greeter("Hello"). Call both with your name and print.
# 3. Write a function make_counter() that returns a function. Each time you call
#    the returned function, it should return the next integer: 0, 1, 2, 3, ...
#    (Use a variable in the enclosing scope that you update. In Python 3 you can use
#    nonlocal to change it.) Create c = make_counter(), then print c(), c(), c().

def make_multiplier(factor):
    def triple(x):
        return factor * x
    return triple

triple = make_multiplier(3)
result = triple(4)
print(result)

def make_greeter(greeting):
    def greeter(name):
        return greeting + ", " + name + "!"
    return greeter

say_hi = make_greeter("Hi")
say_hello = make_greeter("Hello")
print(say_hi("Alex"))
print(say_hello("Alex"))

def make_counter():
    count = 0

    def counter():
        nonlocal count 
        n = count
        count += 1
        return n
    return counter

c = make_counter()
print(c())
print(c())
print(c())
 