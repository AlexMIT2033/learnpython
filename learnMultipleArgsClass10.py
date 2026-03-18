# ============================================================
# Lesson 8: Multiple Function Arguments
# ============================================================
#
# *args: extra positional arguments become a tuple.
#   def f(a, *args): ...   f(1, 2, 3)  -> a=1, args=(2, 3)
#
# **kwargs: extra keyword arguments become a dict.
#   def g(a, **kwargs): ...   g(1, x=2, y=3)  -> a=1, kwargs={'x':2, 'y':3}
#
# You can mix: def h(a, *args, **kwargs): ...
#
# Unpacking when calling:
#   args = (1, 2); f(*args)   passes 1, 2 as two arguments.
#   d = {'x': 1, 'y': 2}; g(**d)   passes x=1, y=2.
#
# ----- YOUR TASKS -----
#
# 1. Write a function greet(*names) that prints "Hello, <name>!" for each name in names.
#    Call greet("Alice", "Bob", "Carol").
# 2. Write a function report(**kwargs) that prints each key and value like "key: value", one per line.
#    Call report(name="Alex", age=10, city="NYC").
# 3. Write a function sum_all(*numbers) that returns the sum of all arguments. Call sum_all(1, 2, 3, 4, 5).
# 4. Write a function build_profile(name, **info) that returns a dict with "name" and all key-value
#    pairs from info. Example: build_profile("Sam", age=9, hobby="chess") -> {"name":"Sam", "age":9, "hobby":"chess"}.

# ----- CONCRETE EXAMPLE -----

def greet(*names):
    for name in names:
        print("Hello, " + name + "!")

def report(**kwargs):
    for key, value in kwargs.items():
        print(key + ": " + str(value))

def sum_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def build_profile(name, **info):
    profile = {"name": name}
    profile.update(info)
    return profile

def test_func(name, address, *numbers, **dict_variable):
    return 1

print("\n--- test functions ---")
print(test_func("Zhibiao", "45TH St",1,2,3,4, age=10, city="NYC"))
name = "Zhibiao"
address = "45TH St"
numbers = (1, 2, 3, 4)
dict_variable = {"age": 10, "city": "NYC"}

# Run the examples: 
print("--- greet ---")
greet("Alice", "Bob", "Carol")

print("\n--- report ---")
report(name="Alex", age=10, city="NYC")

print("\n--- sum_all ---")
print(sum_all(1, 2, 3, 4, 5))

print("\n--- build_profile ---")
print(build_profile("Sam", age=9, hobby="chess"))
