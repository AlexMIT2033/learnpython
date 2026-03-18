# ============================================================
# Simple Class Learning 3 - A Bit Harder!
# Instructions only. Build it yourself – no solution here!
# ============================================================

# ----- PART 1: BUILD THE CLASS -----
#
# 1. Create a class named PiggyBank (a blueprint for a small bank).
#
# 2. Inside the class, write __init__. It should take these inputs (besides self):
#    - owner (the name of the person who owns this piggy bank)
#    - balance (a number: how much money is inside, e.g. 10 or 0)
#    Store each input as a variable that belongs to the piggy bank.
#
# 3. Add a method named show_balance. It should print the owner's name and
#    the current balance. It does not need any inputs besides self.
#
# 4. Add a method named deposit. It should take one extra input: amount (a
#    number). Add that amount to the balance and print a message like
#    "Deposited 5. New balance: 15." It only needs self and amount.
#
# 5. Add a method named withdraw. It should take one extra input: amount (a
#    number). If the balance is at least that amount, subtract it from the
#    balance and print "Withdrew X. New balance: Y." If the balance is less
#    than the amount, do not change the balance; instead print
#    "Not enough in the bank!"

class PiggyBank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print("%s is the owner of this bank. The current balance is %s" % (self.owner, self.balance))

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited %s. New balnce: %s" % (amount, self.balance))      

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount 
            print( "Withdrew %s. New balance: %s" % (amount, self.balance))  
        
        else: 
            print("Not enough in the bank!")
        


# ----- PART 2: HOW TO CALL IT -----
#
# 6. To create a piggy bank: use PiggyBank, then parentheses with owner and
#    balance. Assign the result to a variable (e.g. my_bank).
#
# 7. To show the balance: variable name, dot, show_balance with parentheses.
#
# 8. To deposit: variable name, dot, deposit with parentheses, and inside the
#    parentheses put the amount (e.g. my_bank.deposit(5)).
#
# 9. To withdraw: variable name, dot, withdraw with parentheses, and inside
#    the parentheses put the amount (e.g. my_bank.withdraw(3)).

# ----- YOUR TASKS -----
#
# 10. Create one piggy bank with an owner name and a starting balance (e.g. 0
#     or 10).
#
# 11. Call show_balance to see the starting balance.
#
# 12. Call deposit at least twice with different amounts. After each deposit,
#     call show_balance to see the new balance (or read the message deposit
#     prints).
#
# 13. Call withdraw once with an amount that is OK (less than or equal to the
#     balance). Then call show_balance again.
#
# 14. Call withdraw again with an amount that is too big (more than the
#     balance). You should see "Not enough in the bank!" and the balance should
#     not change. Call show_balance to confirm.

bank1 = PiggyBank("Bob", 40)
bank1.show_balance()
bank1.deposit(10)
bank1.deposit(5)
bank1.withdraw(10)
bank1.show_balance()
bank1.withdraw(60)
bank1.show_balance()
