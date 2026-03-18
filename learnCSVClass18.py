# # ============================================================
# Lesson 16: Parsing CSV Files
# ============================================================

# import csv

# Reading:
#   with open("file.csv", newline="") as f:
#       reader = csv.reader(f)
#       for row in reader:
#           print(row)   # each row is a list of strings

#   with open("file.csv", newline="") as f:
#       reader = csv.DictReader(f)   # first row = headers -> keys
#       for row in reader:
#           print(row["column_name"])

# Writing:
#   with open("out.csv", "w", newline="") as f:
#       writer = csv.writer(f)
#       writer.writerow(["Name", "Age"])
#       writer.writerow(["Alice", 10])

#   with open("out.csv", "w", newline="") as f:
#       writer = csv.DictWriter(f, fieldnames=["Name", "Age"])
#       writer.writeheader()
#       writer.writerow({"Name": "Alice", "Age": 10})

# ----- YOUR TASKS -----

# 1. Create a file "grades.csv" with a text editor or Python: first line "name,score", second "Alice,95", third "Bob,87".
#    Open it with csv.reader, loop over rows, and print each row as a list.
# 2. Open "grades.csv" with csv.DictReader. Loop and print each row as a dict (or print row["name"], row["score"]).
# 3. Use csv.writer to write a new file "favorites.csv" with headers "food", "color" and two rows of your choice.
# 4. Read "favorites.csv" back with csv.DictReader and print each person's food and color.

import csv

with open("grades.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Score"])
    writer.writerow(["Alice", 95])
    writer.writerow(["Bob", 87])

with open("grades.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

