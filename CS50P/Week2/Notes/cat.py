
def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("meow")
        
'''
#infinite loop
while True:
    n = int(input"What is n? ")
    if n > 0:
        break

    #if n < 0:
    #     continue
    #else:
        #break


print("meow\n" * 3, end="")
#becasue default end is \n


for _ in range(3):
    print("meow")
#the _ is the same as i.Its a placeholder for when a variable is uneccesary.


i = 0
while i < 3:
    print("meow")
    i += 1
    #same as i = i + 1
'''