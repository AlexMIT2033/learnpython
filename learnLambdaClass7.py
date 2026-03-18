# ============================================================
# Lesson 6: Lambda functions
# ============================================================
#
# A lambda is a small anonymous function: lambda args: expression
# Only one expression; no statements. Good for short one-off functions.
#
#   f = lambda x: x + 1
#   f(5)   -> 6
#
#   g = lambda a, b: a * b
#   g(3, 4)   -> 12
#
# Often used with map, filter, sorted (see next lesson).
#
# ----- YOUR TASKS -----
#
# 1. Assign to f a lambda that takes one number and returns its square. Call f(4) and print the result.
# 2. Assign to add a lambda that takes two numbers and returns their sum. Call add(10, 20) and print.
# 3. Write a lambda that takes a string and returns the string in all caps. Call it with "hello" and print.
# 4. Use sorted() with a list of strings, e.g. ["banana", "apple", "cherry"]. Use key=lambda s: len(s)
#    and print the result. Then use key=lambda s: s[-1] and print (sort by last letter).

f = lambda x: x * x
print(f(4))

task2 = lambda a, b: a + b
print(task2(10, 20))

task3 = lambda x: x.upper()
print(task3("hello"))

task4 = sorted(["banana", "apple", "cherry"], key = lambda s: len(s))
print(task4)

task5 = sorted(["bananx", "apple", "cherry"], key = lambda s: s[-1])
print(task5)
