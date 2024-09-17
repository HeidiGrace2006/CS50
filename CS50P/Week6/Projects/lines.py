import sys

def main():
    check_input()
    print (f"{sys.argv[1]} has {count()} lines of code.")

def check_input():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file.")
    else:
        try:
            with open(sys.argv[1], "r") as file:
                return True
        except FileNotFoundError:
            sys.exit("File does not exist.")

def count():
    line_count = 0
    with open(sys.argv[1], "r") as file:
        for line in file:
            if not line.lstrip().startswith("#") and len(line.strip()) != 0:
                line_count += 1
    return line_count

if __name__ == "__main__":
    main()

