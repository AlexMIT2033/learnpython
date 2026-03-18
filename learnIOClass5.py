# ============================================================
# Lesson 1: Input and Output
# ============================================================
#
# INPUT
#   input("prompt")  reads one line from the user and returns it as a string.
#   To get a number, use int(...) or float(...) around input(...).
#
# OUTPUT
#   print(x)         prints x and a newline.
#   print(a, b, c)   prints several values separated by spaces.
#   print(..., end="")  no newline at the end.
#   print(..., sep="|")  use "|" between items instead of space.
#
# FILES (basic)
#   open("filename.txt")           open for reading (default).
#   open("filename.txt", "w")      open for writing (overwrites).
#   open("filename.txt", "a")      open for appending.
#   f.read()    read entire file as one string.
#   f.readline()  read one line.
#   f.readlines()  read all lines as a list.
#   f.write("text")  write a string (no newline unless you add \n).
#   f.close()   close the file (or use "with open(...) as f:" to auto-close).
#
# ----- YOUR TASKS -----
#
# 1. Ask the user for their name with input, then print "Hello, <name>!".
# 2. Ask for two numbers (as strings, then convert to int). Print their sum.
# 3. Open a new file "hello.txt" for writing, write "Hello, file!" and a newline, then close it.
# 4. Open "hello.txt" for reading, read and print its contents, then close it.
# 5. Use "with open('hello.txt','a') as f:" and append one more line. Then read the file again and print it.

alex = input("Your name: ")
print("Hello, " + alex + "!")

x = int(input("Number 1: "))
y = int(input("Number 2: "))
z = int(input("Number 3: "))
print(x + y + z)

f = open("hello.txt", "w")
f.write("Hello alex \n")
f.close()

f = open("hello.txt")
contents = f.read()
print(contents)
f.close()


# # ----- SOLUTIONS -----

# # 1.
# name = input("Your name: ")
# print("Hello, " + name + "!")

# # 2.
# a = int(input("First number: "))
# b = int(input("Second number: "))
# print(a + b)

# # 3.
# f = open("hello.txt", "w")
# f.write("Hello, file!\n")
# f.close()

# # 4.
# f = open("hello.txt")
# contents = f.read()
# print(contents)
# f.close()

# # 5.
# with open("hello.txt", "a") as f:
#     f.write("One more line.\n")
# with open("hello.txt") as f:
#     print(f.read())
