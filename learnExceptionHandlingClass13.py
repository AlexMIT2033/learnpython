# ============================================================
# Lesson 3: Exception Handling
# ============================================================
#
# When something goes wrong, Python raises an exception. You can catch it so
# the program doesn't crash.
#
#   try:
#       risky_code()
#   except SomeError:
#       handle_it()
#
#   try:
#       ...
#   except ValueError as e:
#       print("ValueError:", e)
#   except ZeroDivisionError:
#       print("Divided by zero")
#   finally:
#       print("Always runs")
#
# Common: ValueError, TypeError, ZeroDivisionError, FileNotFoundError, KeyError, IndexError.
# You can raise: raise ValueError("message")
#
# ----- YOUR TASKS -----
#
# 1. Write a try/except that asks the user for a number with input(), converts
#    to int(), and prints "You entered: <n>". If they type something that isn't
#    a number, catch ValueError and print "That wasn't a number."
# 2. Write a function safe_divide(a, b) that returns a/b. If b is 0, catch
#    ZeroDivisionError and return None (or print a message and return None).
# 3. Open a file "nonexistent.txt" for reading inside a try. Catch FileNotFoundError
#    and print "File not found." Otherwise read and print the first line.
# 4. Write a short try/except/finally. In try: print "try". In except: print "except".
#    In finally: print "finally". Run it. Then change try to raise ValueError()
#    and run again; confirm finally still runs.

try:
    a = input()
    a_int = int(a)
    print("You entered %s." % a_int)
except ValueError as e:
    print("That wasn't a number. ")
