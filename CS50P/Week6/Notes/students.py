'''
#CSV... comma separated values
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

#alternatively..
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

#sorted.. (list)
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)

#as keys.. (dictionary)
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        # student = {"name": name, "house": house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")
.
.
.
#Sort by using key
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})

#function returns they key name
def get_name(student):
    return student["name"]

#in the sorted function.. the function get_name is telling to sort by the key name
#no need for () after get_name... sorted is calling it for you
for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")
#OR.. for student in sorted(students, key=lambda student: student["name"]):
#"lambda" means anonymous funct. Used when creating a whole named funct. is unneces.
.
.
.
#uses reader function to sort through what should or shouldnt be sep.
import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "home": row[1]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

#use DictReader to name "rows" .. in csv add "name, home" at the top.
import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")
.
.
.
'''
#finallyyyy.. write CSV
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})