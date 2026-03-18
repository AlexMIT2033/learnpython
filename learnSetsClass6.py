# ============================================================
# Lesson 4: Sets
# ============================================================
#
# A SET is a collection of unique items (no duplicates). Unordered. Mutable.
#
#   s = {1, 2, 3}
#   s = set([1, 2, 2, 3])   -> {1, 2, 3}
#
#   s.add(4)      add one item
#   s.remove(2)   remove (error if missing)
#   s.discard(2)  remove if present (no error)
#   x in s       membership
#
#   a | b   union (all in either)
#   a & b   intersection (in both)
#   a - b   difference (in a, not in b)
#   a ^ b   symmetric difference (in one, not both)
#
# ----- YOUR TASKS -----
#
# 1. Create a set of your favorite fruits (strings). Print it. Add one more fruit.
#    Check if "apple" is in the set (print True or False).
# 2. From the list [1, 2, 2, 3, 3, 3, 4], build a set and print it. What happens to duplicates?
# 3. Create two sets: A = {1, 2, 3}, B = {2, 3, 4}. Print A | B, A & B, A - B, B - A.
# 4. Write a function that takes a list and returns a new list with duplicates
#    removed (order doesn't matter). Use a set. Example: [1,2,2,3,1] -> [1,2,3] or [2,1,3].

s = {"pineapples", "watermelon" }
print(s)
s.add("blueberries")
print(s)
print( "apple" in s)      

A = {1,2,3}
B = {2,3,4}
print( A | B)
print(A & B)
print(A - B)
print(B - A)