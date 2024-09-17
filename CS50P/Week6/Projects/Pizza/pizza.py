from tabulate import tabulate
import sys
import csv

def main():
    menu = []
    
    check_input()
    print (format(menu))

def check_input():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file.")
    else:
        try:
            open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("File does not exist.")

def format(menu):
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            menu.append(row)
    menu_formatted = (tabulate(menu, headers = "keys", tablefmt = "grid"))
    return menu_formatted

if __name__ == "__main__":
    main()


