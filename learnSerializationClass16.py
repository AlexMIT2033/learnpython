# ============================================================
# Lesson 14: Serialization
# ============================================================
#
# Serialization = turning data (e.g. dict, list) into bytes or text so you can
# save to a file or send over the network. Deserialization = back to Python objects.
#
# JSON (text, human-readable, safe for sharing):
#   import json
#   json.dumps(obj)       -> string
#   json.loads(string)    -> Python object
#   json.dump(obj, file)   write to file
#   json.load(file)       read from file
#
# Pickle (Python-only, can save almost any object):
#   import pickle
#   pickle.dumps(obj)     -> bytes
#   pickle.loads(bytes)   -> object
#   pickle.dump(obj, file)  /  pickle.load(file)
#
# ----- YOUR TASKS -----
#
# 1. Create a dict: data = {"name": "Alex", "age": 10, "pets": ["cat", "dog"]}.
#    Use json.dumps(data) and print the string. Then use json.loads on that string
#    and print the result (should be a dict again).
# 2. Write data to a file "data.json" using json.dump. Then open "data.json" for reading,
#    use json.load to read it back, and print the loaded object.
# 3. Create a list [1, 2, "hello", {"a": 1}]. Use pickle.dumps to get bytes, then pickle.loads
#    to get the list back. Print the result.
# 4. (Optional) Save a small dict to "data.pkl" with pickle.dump (open file in "wb" mode).
#    Read it back with pickle.load (open in "rb") and print.

import json 

data = {"name": "Alex", "age": 10, "pets": ["cat", "dog"]}
test = json.dumps(data)
print(test)
b = json.loads(test)
print(b)

with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json") as f:
    loaded = json.load(f)
print(loaded)

import pickle
alist = [1, 2, "hello", {"a", 1}]
hi = pickle.dumps(alist)
task3 = pickle.loads(hi)
print(task3)