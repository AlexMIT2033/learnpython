"""
============================================================
Project: Number Guessing Game (Easy)
For a 10-year-old Python learner
Instructions only — you write all the code!
============================================================

HOW TO USE THIS FILE
--------------------
1. Read each PART and each STEP carefully.
2. After a STEP tells you what to do, go underneath this big
   comment and type the Python code yourself.
3. Run the file often to test small pieces as you build.
4. If something breaks, read the STEP again and fix it.
"""

# -----------------------------------------------------------
# PART 1: WELCOME THE PLAYER
# -----------------------------------------------------------
#
# STEP 1:
#   At the very top of your code (BELOW this comment), import
#   the module that lets Python pick random numbers.
#   - The module name is "random".
#   - You have used "import ____" before.

# STEP 2:
#   Print a welcome message for the player.
#   - Example idea (but WRITE YOUR OWN WORDS):
#       "Welcome to the Number Guessing Game!"
#   - Also print a line that explains the rules, such as:
#       "I'm thinking of a number between 1 and 20."
#
# STEP 3:
#   Ask the player for their name using input().
#   - Save the result in a variable (for example: player_name).
#   - Then print a friendly message that uses their name.
#
# (TYPE YOUR CODE FOR PART 1 UNDER THIS LINE)





# -----------------------------------------------------------
# PART 2: PICK A SECRET NUMBER
# -----------------------------------------------------------
#
# STEP 4:
#   Decide what range you want for the secret number.
#   - For example: 1 to 20 (easy) or 1 to 50 (harder).
#   - Remember this range; you will tell the player too.
#
# STEP 5:
#   Use the random module to choose a secret whole number
#   inside your chosen range.
#   - Store this number in a variable (for example: secret_number).
#
# STEP 6:
#   Create a variable to count how many guesses the player uses.
#   - Start it at 0.
#
# (TYPE YOUR CODE FOR PART 2 UNDER THIS LINE)




# -----------------------------------------------------------
# PART 3: MAKE THE GUESSING LOOP
# -----------------------------------------------------------
#
# STEP 7:
#   You want the player to guess again and again until they
#   get the number right.
#   - Use a while-loop for this.
#   - There are two common ways:
#       a) while True:   (and break when correct), OR
#       b) while some_condition_is_true:
#   - Choose ONE style and stick with it.


      

# STEP 8:
#   Inside the loop, ask the player to "Take a guess:" using input().
#   - Save their answer in a variable (for example: guess_text).
#
# STEP 9:
#   Make sure the guess is actually made of digits.
#   - If the player types something like "hello" or "7abc",
#     tell them it is not a valid number and ask again.
#   - Hint: you have seen .isdigit() before.
#
# STEP 10:
#   When the text is valid, turn it into an integer using int().
#   - Save it in a variable (for example: guess).
#   - Add 1 to your "attempts" counter each time they make a
#     valid guess.





# STEP 11:
#   Use if / elif / else to compare guess to secret_number:
#   - If guess is less than secret_number, print something like
#       "Too low! Try again."
#   - Else if guess is greater than secret_number, print
#       "Too high! Try again."
#   - Else (that means it is equal), print a winning message.
#       - Also print how many guesses it took.
#       - Then end the loop so the game round finishes.
#
# (TYPE YOUR CODE FOR PART 3 UNDER THIS LINE)



# -----------------------------------------------------------
# PART 4: PLAY AGAIN FEATURE
# -----------------------------------------------------------
#
# STEP 12:
#   After the player guesses correctly, ask if they want to
#   play again.
#   - Use input() to ask something like:
#       "Do you want to play again? Type 'yes' or 'no': "
#   - Turn their answer to lowercase so "Yes" and "YES" still work.
#
# STEP 13:
#   Use another while-loop OR an outer game loop to allow
#   multiple rounds.
#   - One idea:
#       - Before you start, set a variable like play_again = "yes".
#       - Wrap your whole "pick secret number + guessing loop"
#         inside a while play_again == "yes": loop.
#       - At the end of each round, ask if they want to play
#         again and update play_again.
#   - If they say no, print a goodbye message and end the game.
#
# (TYPE YOUR CODE FOR PART 4 UNDER THIS LINE)

import random

print("Welcome to my Guessing Game!!! ")

player_name = input("Please enter your name.")
print("Welcome to the Guessing Game, %s!" % player_name)


min_number = input("Please select your smallest integer.")
max_number = input("Please select your largest integer.")
min_valid = min_number.isdigit() 
max_valid = max_number.isdigit()
if not min_valid:
   print("Not valid minimal number.")
if not max_valid:
   print("Not valid maximal number.")

min_number = int(min_number)
max_number = int(max_number)

print("The range is from %d to %d." % (min_number, max_number))

play_again = "yes"
while play_again == "yes":
   secret_number =  random.randint(min_number, max_number)
   count = 0

   while True: 
      print("Take a guess!")
      guess_text = input()
      valid = guess_text.isdigit()
      if not valid:
         print("<Error 404> This is not a valid number.")
      else:
         guess = int(guess_text)
         count += 1

         if guess < secret_number:
            print("Too low! Please try again.")

         elif guess > secret_number:
            print("Too high! Please try again.")
         else:
            print("Congratulations! It took you %d guesses." % count)
            print("GAME OVER. YOU WON!!!")
            break  
   
   play_again = input("Do you want to play again? Type 'yes' or 'no'.").lower()
   if play_again != "yes":
      print("Goodbye!")
      break


#
# CHALLENGE D (HARDER):
#   - Keep track of the "best score": the smallest number of
#     guesses the player has ever used.
#   - Show the best score at the end of each round.
#   - Hint: you need a variable that starts as None or a big
#     number, and you update it when the player beats their best.
# -----------------------------------------------------------
# PART 5: EXTRA CHALLENGES (WHEN THE BASIC GAME WORKS)
# -----------------------------------------------------------
#
# Do NOT do all of these at once. Pick ONE challenge, finish it,
# then move to another.
#
# CHALLENGE A (EASY):
#   - Make a special message if the player wins in just ONE guess.
#   - After they win, check if attempts == 1 and print something
#     like "Amazing! You got it in one guess!"
#
# CHALLENGE B (MEDIUM):
#   - Make the game say something different if the player needs
#     more than 7 guesses.
#   - For example:
#       "You got it! Keep practicing to get faster."
#
# CHALLENGE C (MEDIUM):
#   - Let the player choose the range.
#   - Ask them for a maximum number at the beginning of the game.
#   - Use that maximum with your random number.
#
# CHALLENGE D (HARDER):
#   - Keep track of the "best score": the smallest number of
#     guesses the player has ever used.
#   - Show the best score at the end of each round.
#   - Hint: you need a variable that starts as None or a big
#     number, and you update it when the player beats their best.