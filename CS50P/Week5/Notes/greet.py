def main():
    name = input("What's your name? ")
    print(hello(name))

#this means that if name is not given, the default of "to" is "world".
def hello(to="world"):
    #note that this line is in place of .. print("hello,", to)
    #that's because the testing program needs a return value to test
    return f"hello, {to}"


if __name__ == "__main__":
    main()