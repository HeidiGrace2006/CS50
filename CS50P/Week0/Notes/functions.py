
#what you CAN pass = parameters
#what you DO pass = argument
#a function that is built in = method

name = input("What's your name? ")
#remove spaces and capitalize users name
name = name.strip().title()

#split name into first and last names
first, last = name.split(' ')

print("Hello " + name)
#Has same effect... because comma makes it "2 arguments"
#So it adds a space
print("Goodbye", name,)

#In a function.. read documentation to understand
#what the build in function does.
#ex.) print(*objects, sep=' ', end='\n' ....(rest for later)

print("hello")
print(name)
print("goodbye ", end="")
print(name)

#format string... f
number = input("Pick a number from 1-10 ")
print(f"You chose {number}")

#Defining and calling your OWN function with def
#hello () is the function.. (to) is the paraemeter created
#hello(name) calls the function hello with the parameter of saying hello to name. Name = to
#to="world" means that if nothing is assigned to "to" (name), then the default value of to = world
def hello(to="world"):
    print ("hello")

hello(name)

#as good habit.. def main(): at the beginning of code and call main() at the end