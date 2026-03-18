# ============================================================
# Simple Class Learning 2 - For 5th Grade!
# Instructions only. Build it yourself – no solution here!
# ============================================================

# ----- PART 1: BUILD THE CLASS -----
#
# 1. Create a class named Snack (a blueprint for snacks).
#
# 2. Inside the class, write __init__. It should take these inputs (besides self):
#    - name (e.g. "gummy worms", "chips")
#    - flavor (e.g. "sour", "salty")
#    - amount (a number: how many pieces or servings are left)
#    Store each input as a variable that belongs to the snack (so each snack has
#    its own name, flavor, and amount).
#
# 3. Add a function (method) named describe. It should print a sentence that
#    says the snack's name, flavor, and amount. It does not need any inputs
#    besides self.
#
# 4. Add a function (method) named eat_one. It should subtract 1 from the
#    snack's amount and print a message like "Yum! One less." It does not need
#    any inputs besides self. (You can assume there is at least 1 left.)

class Snack:
    def __init__(self, name, flavor, amount):
        self.name = name
        self.flavor = flavor
        self.amount = amount

    def describe(self):
        print("%s is a %s snack and there is %s snacks left." % (self.name , self.flavor , self.amount))
        
    def eat_one(self):
        new_amount = self.amount - 1
        print("Delicious! Now there is one less, %s" % (new_amount))
       

# ----- PART 2: HOW TO CALL IT -----
#
# 5. To create a snack: use the class name Snack, then parentheses with the
#    name, flavor, and amount in that order. Assign the result to a variable
#    (e.g. my_snack).
#
# 6. To make a snack describe itself: write the variable name, a dot, then
#    describe with parentheses.
#
# 7. To eat one of a snack: write the variable name, a dot, then eat_one with
#    parentheses.


# ----- YOUR TASKS -----
#
# 8. Create at least two snacks with different names, flavors, and amounts.
#
# 9. Call describe on each snack so they describe themselves.
#
# 10. Call eat_one on one of your snacks, then call describe again on that
#     snack to see the new amount.

snack1 = Snack("chips", "salty", 5)
snack1.describe()
snack1.eat_one()

snack2 = Snack("cream", "sweet", 7)
snack2.describe()
snack2.eat_one()