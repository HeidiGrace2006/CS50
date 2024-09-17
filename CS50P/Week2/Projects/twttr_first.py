
#input from user
response = input("Input: ")

#print output
print ("Output:", end = "")

#create list of vowels
vowels = ["a", "e", "i", "o", "u"]

#iterate thru input and remove vowels
for char in response:
    if char.lower() not in vowels:
        print(char, end = "",)

print()
