# ============================================================
# Lesson 15: Code Introspection
# ============================================================
#
# Introspection = inspecting objects at runtime: names, types, docstrings, etc.
#
#   type(obj)           -> type of obj
#   dir(obj)            -> list of attribute names
#   hasattr(obj, 'name') -> True if obj has attribute 'name'
#   getattr(obj, 'name') -> value of obj.name (or use default)
#   callable(obj)       -> True if obj can be called (e.g. a function)
#
#   obj.__doc__         docstring
#   obj.__name__        name of function/class (if it has one)
#
# ----- YOUR TASKS -----
#
# 1. Create a list L = [1, 2, 3]. Print type(L). Print dir(L) (or first 10 names).
# 2. Define a function def add(a, b): return a + b. Print add.__name__. Print type(add).
#    Use callable(add) and callable(L) and print the results.
# 3. For the list L, use hasattr(L, "append") and hasattr(L, "xyz"). Print both.
#    Use getattr(L, "append") and print what you get (should be the method). Then getattr(L, "pop")(). What does that do?
# 4. Create a simple class with a docstring. Create an instance. Print the class's __doc__ and the instance's __class__.__name__.

L = [1, 2, 3]
task = type(L)
task1 = dir(L)
print(task)
print(task1)

def add(a, b): 
    return a + b

print(add.__name__)
print(type(add))

task2 = callable(add)
tasks = callable(L)
print(task2)
print(tasks)

pretask = hasattr(L, "append")
task3 = hasattr(L, "xyz")
print(pretask)
print(task3)

it = getattr(L, "append")
print(it)
task3p2 = getattr(L, "pop")()
print(task3p2)