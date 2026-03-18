# ============================================================
# Lesson 12: Generators
# ============================================================
#
# A generator is a function that uses yield instead of return. Each time you
# ask for the "next" value, it runs until the next yield and gives that value,
# then pauses. Good for big or infinite sequences without storing everything.
#
#   def count_up_to(n):
#       i = 0
#       while i < n:
#           yield i
#           i += 1
#
#   list(count_up_to(5))   -> [0, 1, 2, 3, 4]
#
#   g = count_up_to(3)
#   next(g)   -> 0
#   next(g)   -> 1
#   next(g)   -> 2
#   next(g)   -> StopIteration
#
# Generator expression: (x*x for x in range(5))  -> lazy, like a one-line generator.
#
# ----- YOUR TASKS -----
#
# 1. Write a generator evens(n) that yields 0, 2, 4, 6, ... up to (but not including) n.
#    Convert it to a list with list(evens(10)) and print the list.
# 2. Write a generator that yields the squares of 0, 1, 2, 3, ... (no upper limit). Use a while True
#    loop and yield i*i; then i += 1. Get the first 5 values with a for-loop that breaks after 5, or use
#    a list and take [:5] from an infinite generator (trick: use itertools.islice or a loop).
# 3. Use a generator expression (x**2 for x in range(5)). Assign it to g. Call next(g) several times
#    and print each value until you get StopIteration (or loop with for x in g: print(x)).

def evens(n):
    i = 0
    while i < n:
        if i%2 == 0:
            yield i
        i += 1

g = evens(9)
print(next(g))
print(next(g))
print(next(g))