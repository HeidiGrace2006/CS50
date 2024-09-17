
#get input in camelCase
response = input("calmelCase: ")

#have "snake_case" print out beforehand
print("snake_case: ", end = "")

#remember.. this is how string itteration works.
#this for loop is setting "char" equal to each letter in "response". Example:
   #s = ("buzz")
   #for char in s:
      #print(char)
    #. . . So char equals b (prints), then u (prints), etc

for char in response:
    #if upper.. fix it
    if char.isupper():
        print("_" + char.lower(), end = "")
    #else, just print
    else:
        print(char, end = "")

#move to next line
print()
