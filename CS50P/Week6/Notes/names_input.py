'''
#Problem: re-writes program every time its opened
name = input("What's your name? ")
file = open("names.txt", "w")
file.write(name)
file.close()

#Problem: you could forget to close the file
name = input("What's your name? ")
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
.
.
.
#Using with and as..
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())

#Cleaned up
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())

'''
#Sorted
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
