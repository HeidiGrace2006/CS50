Set
    #datatype used in place of a list for no repeats
Global variable
    #With a GV, you can read it (call it) in other functions but not write it (change it)
    Solution:
        #Put 'global' in front of variable. Ex):
            balance = 0
            def main():
                print("Balance:", balance)
                deposit(100)
                withdraw(50)
                print("Balance:", balance)

            def deposit(n):
                global balance
                balance += n
            def withdraw(n):
                global balance
                balance -= n
        #As a class:
            class Account:
                def __init__(self):
                    self._balance = 0
                @property
                def balance(self):
                    return self._balance
                def deposit(self, n):
                    self._balance += n
                def withdraw(self, n):
                    self._balance -= n

            def main():
                account = Account()
                print("Balance:", account.balance)
                account.deposit(100)
                account.withdraw(50)
                print("Balance:", account.balance)
Datatype hints & MyPy
    #When you declare a variable, express what type of variable it should be
    #Since python doesnt check this, use mypy
    def meow(n: int):
        for _ in range(n):
            print("meow")

        number: int = int(input("Number: "))
        print(meows)
        #run mypy meows.py

Docstrings
    #docstring comments are """ comments """
    #formatting doc strings:
    def meow(n):
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    #return "meow\n" * n

    def main():
        number = int(input("Number: "))
        meows = meow(number)
        print(meows, end="")

Argparse
    #Used to make sys.args more useable
    import argparse

    parser = argparse.ArgumentParser(description="Meow like a cat")
    parser.add_argument("-n", default=1, help="number of times to meow", type=int)
    args = parser.parse_args()

    for _ in range(args.n):
        print("meow")
    #try typing '-h' or '--help' when running the program. (python meows.py --help). It will show you the usage
Unpacking
    #To unpack a list or some other type so that it's passed through 1 by 1
    def total(galleons, sickles, knuts):
        return (galleons * 17 + sickles) * 29 + knuts

    #for list:
    coins = [100, 50, 25]
    print(total(*coins), "Knuts")
    #rather than: print(total(coins[0], coins[1], coins[2]), "Knuts")
    # the '*' unpacks the list.

    #for dict:
    def total(galleons, sickles, knuts):
    #return (galleons * 17 + sickles) * 29 + knuts

    coins = {"galleons": 100, "sickles": 50, "knuts": 25}
    print(total(**coins), "Knuts")
    #rather than: print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")
Args and Kwargs
    #args are positional arguments, such as those we provide to print like print("Hello", "World"
    #kwargs are named arguments, or “keyword arguments”, such as those we provide to print like print(end="")

    #'*' can be used as a place holder for "some number of ___ (argurments)"
    #args is positional, kwargs is named
    def f(*args, **kwargs):
        print("Positional:", args)
    f(100, 50, 25)

    def f(*args, **kwargs):
        print("Named:", kwargs)
    f(galleons=100, sickles=50, knuts=25)
Map
    def main():
        # yell("This", "is", "CS50")

    #def yell(*words):
        yell(["This", "is", "CS50"])

    def yell(words):
        uppercased = []
        for word in words:
            uppercased.append(word.upper())
        print(*uppercased)
    main()

        #with map, you can "map" (or copy and paste) a trait onto something else. In this case, uppercase onto words
    def main():
        yell("This", "is", "CS50")

    def yell(*words):
        uppercased = map(str.upper, words)
        print(*uppercased)
List comprehension
    #an easy way to skip uppercasing and appending everything

    #new_list = [expression for item in iterable if condition]
        #expression: The value you want to include in the new list.
        #item: Variable representing each element in the iterable.
        #iterable: The sequence you are iterating over.
        #if condition: An optional condition to filter elements.
        
    def main():
    yell("This", "is", "CS50")

    def yell(*words):
        uppercased = [arg.upper() for arg in words]
        print(*uppercased)

    main()

    #Another ex.)
    students = [
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherin"},
    ]
    #gryffindors = []
    #for student in students:
        #if student["house"] == "Gryffindor":
            #gryffindors.append(student["name"])
    gryffindors = [
        student["name"] for student in students if student["house"] == "Gryffindor"
    ]

    for gryffindor in sorted(gryffindors):
        print(gryffindor)
Filter
    #Filter is like map, but takes true or false. 'include if true'.
    students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    ]

    def is_gryffindor(s):
        #this returns True or False.. replaces 'if __: return True'.
        return s["house"] == "Gryffindor"

    #the filter is, if the function is_gryf returns true.. include the student.
    gryffindors = filter(is_gryffindor, students)

    #alternatively, to elim is_gryf funct:
    #gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

    #lambda.. anonymous function
    for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
        print(gryffindor["name"])
Dictionary Comprehension
    students = ["Hermione", "Harry", "Ron"]

    gryffindors = []

    #List of dictionary objects
    gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
    #rather than:
    #for student in students:
        #gryffindors.append({"name": student, "house": "Gryffindor"})

    #OR.. one big dictionary object:
    #gryffindors = {student: "Gryffindor" for student in students}

    print(gryffindors)
Enumerate
    students = ["Hermione", "Harry", "Ron"]

    for i, student in enumerate(students):
    print(i + 1, student)

    #for i in range(len(students)):
        #print(i + 1, students[i])
Generators and yield
#Generate MASSIVE amounts of data.. returns a *little* at a time, so that your pc doesnt go boom.
    n = int(input("What's n? "))
    for i in range(n):
        print("🐑" * i)

    #with funct:
    def main():
        n = int(input("What's n? "))
        for s in range(n):
            print(sheep(s))

    def sheep(n):
        return "🐑" * n

    main()

    #Return sheep as list
    def main():
        n = int(input("What's n? "))
        for s in sheep(n):
            print(s)

    def sheep(n):
        flock = []
        for i in range(n):
            flock.append("🐑" * i)
        return flock

    #SOLUTION:
    #def sheep(n):
        #for i in range(n):
            #yield "🐑" * i

    main()
Fun!
    import cowsay
    import pyttsx3

    engine = pyttsx3.init()
    this = input("What's this? ")
    cowsay.cow(this)
    engine.say(this)
    engine.runAndWait()