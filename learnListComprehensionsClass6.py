# ============================================================
# Lesson 5: List Comprehensions
# ============================================================
#
# A list comprehension builds a list in one line: [expression for item in iterable].
#
#   squares = [x * x for x in range(5)]     -> [0, 1, 4, 9, 16]
#   evens   = [x for x in range(10) if x % 2 == 0]
#   words   = [w.upper() for w in ["a", "b", "c"]]
#
# You can add "if" at the end: [x for x in ... if condition]
# You can use two loops: [ (i,j) for i in range(2) for j in range(2) ]
#
# Similar: {key: value for ...}  dict comprehension
#          (x for x in ...)      generator expression (see Generators lesson)
#
# ----- YOUR TASKS -----
#
# 1. Build a list of squares of 0..9 using a list comprehension. Print it.
# 2. From the list [3, 1, 4, 1, 5], build a new list with each number doubled. Use a comprehension.
# 3. From range(10), build a list of only the odd numbers. Use a comprehension with "if".
# 4. From ["apple", "banana", "cherry"], build a list of the lengths of each word. Use a comprehension.
# 5. From a list of numbers (e.g. [1, -2, 3, -4, 5]), build a list of only the positive numbers. Use "if".

task1 = [x * x for x in range(10)]
print(task1)

task2 = [ x * 2 for x in [3, 1, 4, 1, 5] ]
print(task2)

task3 = [ x for x in range(10) if x % 2 == 1]
print(task3)

task4 = [len(x) for x in [ "apple", "banana", "cherry"]]
print(task4)

task5 = [ x for x in [1, -2, 3, -4, 5] if x > 0]
print(task5)