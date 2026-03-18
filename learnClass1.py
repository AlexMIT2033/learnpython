# ============================================================
# Simple Class Learning - For 5th Grade!
# Instructions only. Build it yourself – no solution here!
# ============================================================

# ----- PART 1: BUILD THE CLASS -----
#
# 1. Create a class named Pet (a blueprint for making pets).
#
# 2. Inside the class, write __init__. It should take these inputs (besides self):
#    - name
#    - animal_type (e.g. dog, cat, dragon)
#    - age
#    Store each input as a variable that belongs to the pet (so each pet has its
#    own name, animal_type, and age).
#
# 3. Add a function (method) named introduce. It should print a sentence that
#    says the pet’s name, age, and animal type. It does not need any inputs
#    besides self.
#
# 4. Add a function (method) named have_birthday. It should add 1 to the pet’s
#    age and print a birthday message. It does not need any inputs besides self.

class Pet:
    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age
    
    def introduce(self):
        print("I'm %s, a %s year old %s." % (self.name, self.age, self.animal_type))

    def have_birthday(self):
        new_age = 1 + self.age
        print("happy birthday! you are now %s" % (new_age))


# ----- PART 2: HOW TO CALL IT -----
#
# 5. To create a pet: use the class name Pet, then parentheses with the name,
#    animal_type, and age in that order. Assign the result to a variable
#    (e.g. my_pet).
#
# 6. To make a pet introduce itself: write the variable name, a dot, then
#    introduce with parentheses.
#
# 7. To give a pet a birthday: write the variable name, a dot, then
#    have_birthday with parentheses.



# ----- YOUR TASKS -----
#
# 8. Create at least two pets with different names, types, and ages.
#
# 9. Call introduce on each pet so they introduce themselves.
#
# 10. Call have_birthday on one of your pets, then call introduce again on
#     that pet to see the new age.
pet1 = Pet("Charles", "dragon", 5)
pet1.introduce()
pet1.have_birthday()

pet2 = Pet("John", "hamster", 4)
pet2.introduce()
pet2.have_birthday()