"""
============================================================
Project: Treasure in the Forest (Medium)
Text Adventure Game for a 10-year-old
Instructions only — you write all the code!
============================================================

HOW TO USE THIS FILE
--------------------
1. This is a "choose your own adventure" game.
2. Read each PART and each STEP carefully.
3. After a STEP tells you what to do, go underneath this big
   comment and type the Python code yourself.
4. Run the file often to test scenes as you build them.
"""

# -----------------------------------------------------------
# PART 1: GLOBAL VARIABLES AND HELPER FUNCTION
# -----------------------------------------------------------
#
# STEP 1:
#   Create a variable that will be a list to hold items the
#   player finds. This is your "backpack" or inventory.
#   - Example variable name: inventory
#   - Start it as an empty list.
#
# STEP 2:
#   Create a variable to hold the player's name.
#   - Example variable name: player_name
#   - You can start it as an empty string.
#
# STEP 3:
#   Write a helper function to ask the player for a choice:
#   - Name idea: ask_choice
#   - It should take two inputs:
#       1) a prompt string (the question)
#       2) a list of allowed answers (like ["left", "right"])
#   - Inside the function:
#       - Use input() to get the player's answer.
#       - Turn the answer to lowercase using .lower().
#       - While the answer is NOT in the allowed list:
#           * Print a message that tells them what the valid
#             options are.
#           * Ask again.
#       - When the answer is valid, return it.
#
# (TYPE YOUR CODE FOR PART 1 UNDER THIS LINE)



# -----------------------------------------------------------
# PART 2: START FUNCTION (INTRO + NAME)
# -----------------------------------------------------------
#
# STEP 4:
#   Write a function that starts the adventure.
#   - Name idea: start
#   - Inside this function:
#       a) Print a welcome message for the game.
#       b) Ask the player for their name using input().
#       c) Store the name in your player_name variable.
#          (Hint: you may need to use the word "global" inside
#           the function to modify the variable defined above.)
#       d) Print a line that greets them by name and explains
#          that their goal is to find a treasure.
#       e) At the end of this function, call another function
#          that will show the first scene, such as
#          forest_entrance().
#
# (TYPE YOUR CODE FOR PART 2 UNDER THIS LINE)



# -----------------------------------------------------------
# PART 3: FOREST ENTRANCE SCENE
# -----------------------------------------------------------
#
# STEP 5:
#   Write a function for the first scene.
#   - Name idea: forest_entrance
#   - Inside this function:
#       a) Print a short description of where the player is.
#          (For example: at the edge of a dark forest.)
#       b) Explain at least two paths:
#            - One path goes into the forest.
#            - One path goes along a river.
#       c) Use your ask_choice helper to ask:
#            "Do you go left or right?"
#            and allow answers like ["left", "right"].
#       d) If the player chooses "left", call a function that
#          will handle the deep forest scene (you will write
#          this next).
#          If the player chooses "right", call the river scene.
#
# (TYPE YOUR CODE FOR PART 3 UNDER THIS LINE)



# -----------------------------------------------------------
# PART 4: RIVER PATH SCENE
# -----------------------------------------------------------
#
# STEP 6:
#   Write a function for the river scene.
#   - Name idea: river_path
#   - Inside this function:
#       a) Describe the river (clear water, sounds, etc.).
#       b) Describe something interesting, like a shiny object
#          in the water.
#       c) Use ask_choice to ask the player whether they:
#            - "pick" (pick it up), or
#            - "ignore" (leave it alone).
#       d) If they pick it up:
#            - Print a message that they found a golden key.
#            - Add the word "key" to your inventory list if it
#              is not already there.
#            - Then send the player back to the forest entrance
#              by calling forest_entrance().
#       e) If they ignore it:
#            - Print a message that they walk away.
#            - Then send them back to forest_entrance().
#
# (TYPE YOUR CODE FOR PART 4 UNDER THIS LINE)



# -----------------------------------------------------------
# PART 5: DEEP FOREST + CAVE ENTRANCE
# -----------------------------------------------------------
#
# STEP 7:
#   Write a function for walking deeper into the forest.
#   - Name idea: deep_forest
#   - Inside this function:
#       a) Print a description of the deeper forest.
#       b) Explain that they see a cave entrance in a hill.
#       c) Use ask_choice to ask:
#            "Do you go into the cave or go back?"
#            and allow answers like ["cave", "back"].
#       d) If they choose "cave", call your cave() function
#          (you will write that next).
#       e) If they choose "back", send them to
#          forest_entrance().
#
# (TYPE YOUR CODE FOR PART 5 UNDER THIS LINE)



# -----------------------------------------------------------
# PART 6: CAVE AND TREASURE CHEST
# -----------------------------------------------------------
#
# STEP 8:
#   Write a function for the cave scene.
#   - Name idea: cave
#   - Inside this function:
#       a) Print a description of the cave (dark, echoing, etc.).
#       b) Explain that there is a big wooden chest at the back.
#       c) Check if the player has the key:
#            - Look in the inventory list for the word "key".
#       d) If the player HAS the key:
#            - Print that they unlock and open the chest.
#            - Print a victory message that includes their name
#              and says they found the treasure.
#            - Call a function that will end the game and maybe
#              ask if they want to play again.
#       e) If the player DOES NOT have the key:
#            - Print a message that the chest is locked.
#            - Suggest that they might find a key somewhere
#              else (like near the river).
#            - Ask if they want to go back to the forest
#              entrance.
#              * If yes, call forest_entrance().
#              * If no, you can either:
#                  - leave them in the cave and ask again, OR
#                  - create a "stuck" ending.
#
# (TYPE YOUR CODE FOR PART 6 UNDER THIS LINE)



# -----------------------------------------------------------
# PART 7: ENDING THE GAME
# -----------------------------------------------------------
#
# STEP 9:
#   Write a function to handle the end of the game.
#   - Name idea: end_game
#   - Decide what inputs it should have:
#       For example, you can give it a boolean (True/False)
#       that says whether the player won or not.
#   - Inside the function:
#       a) If they won, print a "You completed your adventure!"
#          style message.
#       b) If they lost or got stuck, print a different ending.
#       c) Ask the player if they want to play again:
#            - If yes:
#               * Clear the inventory list so they start fresh.
#               * Call start() again.
#            - If no:
#               * Print a goodbye message and do NOT restart.
#
# (TYPE YOUR CODE FOR PART 7 UNDER THIS LINE)



# -----------------------------------------------------------
# PART 8: STARTING THE PROGRAM
# -----------------------------------------------------------
#
# STEP 10:
#   At the very bottom of the file, write the special lines
#   that start your game when you run this file:
#   - Use the pattern you have seen before with
#       if __name__ == "__main__":
#           ...
#   - Inside that if-block, call your start() function.
#
# (TYPE YOUR CODE FOR PART 8 UNDER THIS LINE)



# -----------------------------------------------------------
# EXTRA CHALLENGES (WHEN YOUR BASIC GAME WORKS)
# -----------------------------------------------------------
#
# Do these ONE AT A TIME. Test after each change.
#
# CHALLENGE A (EASY):
#   - Add more description to your scenes so they feel like a
#     real story. Use at least 3 sentences per scene.
#
# CHALLENGE B (EASY):
#   - Add a new scene, such as an "old tree" or "mysterious hut".
#   - Give the player a new choice at the forest entrance to go
#     there. Maybe they can find a "map" there.
#
# CHALLENGE C (MEDIUM):
#   - Add another item like "map" or "lantern" to inventory.
#   - Make the cave ending change if the player has both "key"
#     and your new item (extra special treasure).
#
# CHALLENGE D (MEDIUM):
#   - Add a way to "lose" the game.
#   - For example, if the player ignores the shiny object at the
#     river too many times, they get lost and the adventure ends.
#   - You will need a variable to count how many times they do
#     something.
#
# CHALLENGE E (HARDER):
#   - Add a "health" or "courage" number that starts at some
#     value (like 3).
#   - In certain scenes (scary ones!), you can subtract 1.
#   - If it reaches 0, the player is too scared or tired to
#     continue and the game ends.

