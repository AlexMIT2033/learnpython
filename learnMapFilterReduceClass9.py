# ============================================================
# Lesson 7: Map, Filter, Reduce
# ============================================================
#
# MAP: apply a function to every item.
#   list(map(lambda x: x * 2, [1, 2, 3]))   -> [2, 4, 6]
#
# FILTER: keep only items where the function is True.
#   list(filter(lambda x: x > 2, [1, 2, 3, 4]))   -> [3, 4]
#
# REDUCE: combine all items into one value (need: from functools import reduce).
#   reduce(lambda a, b: a + b, [1, 2, 3, 4])   -> 10
#   reduce(lambda a, b: a * b, [1, 2, 3, 4])   -> 24
#
# Often you can do the same with a list comprehension: [x*2 for x in lst]
#
# ----- YOUR TASKS -----
#
# 1. Use map to convert the list [1, 2, 3, 4, 5] into a list of squares. Print the result (as a list).
# 2. Use filter to keep only the even numbers from [1, 2, 3, 4, 5, 6]. Print the result as a list.
# 3. Use reduce (import from functools) to compute the product of [1, 2, 3, 4]. Print the result.
# 4. Do task 1 again using a list comprehension instead of map. Do task 2 again using a list comprehension instead of filter.

from functools import reduce
a = list(map(lambda x: x * 2, [1, 2, 3]))
b = list(filter(lambda x: x > 2, [1, 2, 3, 4]))
c = reduce(lambda a, b: a + b, [1, 2, 3, 4])
print(a)
print(b)
print(c)
 
task1 = list(map(lambda x: x * x, [1, 2, 3, 4, 5]))
print(task1)
task2 = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
print(task2)
task3 = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(task3)
