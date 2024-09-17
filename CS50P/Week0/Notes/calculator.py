
x = input("What's x? ")
y = input("What's y? ")

#the + is concatenating (joining) the strings
#so change the strings to int
z = int(x) + int(y)

print (z)

"""
Or, to remove the need for another variable (z):

x = int(input("What's x? "))
y = int(input(What's y? "))

print (x + y)

"""

#float is with a decimal
#documentation: round(number [, ndigits])
print("\n")
num1 = float(input("What is the first number? "))
num2 = float(input("what is the second number? "))

result = round(num1 + num2)

#using an f function to add a comma in between sets of 0's .. test with numbers > 1000
print (f"{result:,}")


"""
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()
"""