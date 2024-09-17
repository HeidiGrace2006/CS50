import re

name = input("What's your name? ").strip()

#if matches := re.search(r"^(.+), *(.+)$", name):   ..... := is the 'walrus' operator. Used to assign and ask boolean in same line
    #name = matches.group(2) + " " + matches.group(1)

#Searching "name" for the right characters.. storing it as matches
matches = re.search(r"^(.+), (.+)$", name)
#if there are matches....
if matches:
    last = matches.group(1)
    first = matches.group(2)
    #last, first = matches.groups()

    name = f"{first} {last}"
print(f"hello, {name}")

'''
name = input("What's your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"

print(f"hello, {name}")
'''