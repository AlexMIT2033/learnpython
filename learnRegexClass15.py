# ============================================================
# Lesson 13: Regular Expressions
# ============================================================
#
# import re
#
# re.search(pattern, string)   -> match object or None (first match)
# re.findall(pattern, string) -> list of all matching substrings (or groups)
# re.sub(pattern, replacement, string) -> new string with replacements
#
# Patterns: \d digit, \w word char, \s space;  + one or more, * zero or more;
#   [0-9], [a-z];  ( ) group;  . any char.  r"..." raw string often used.
#
#   re.search(r"\d+", "I have 42 cats")  -> match "42"
#   re.findall(r"\d+", "a1 b22 c333")     -> ['1', '22', '333']
#   re.sub(r"cat", "dog", "one cat two cats") -> "one dog two dogs"
#
# ----- YOUR TASKS -----
#
# 1. Use re.search to find the first number (one or more digits) in the string "Price is 99 dollars."
#    Print the matched string (use .group() on the match object, or check for None).
# 2. Use re.findall to find all numbers in "I have 2 apples and 3 oranges and 10 grapes." Print the list.
# 3. Use re.sub to replace every "bad" with "good" in "This is bad. Very bad." Print the result.
# 4. Write a pattern that matches a simple email-like string: one or more word chars, @, then word chars, then
#    a dot and "com". Use re.search on "Contact me at alice@example.com today." and print the match.

import re

results = re.search(r"\d+", "Price is 99 dollars.")
print(results.group())

result = re.findall(r"\d+", "I have 2 apples and 3 oranges and 10 grapes.")
print(result)

task3 = re.sub(r"bad", "good", "This is bad. Very bad.")
print(task3)

task4 = re.search(r"\w+@\w+\.com", "Contact me at alice@example.com today.")
print(task4.group())