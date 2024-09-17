import csv
import sys

def main():
    check_input()
    rewrite_info()

def check_input():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit(f"Could not read {sys.argv[1]}")
    else:
        try:
            open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("File does not exist.")

def rewrite_info():
    students = []

    #Read the first file.. split name
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].split(",")
            student = {"first": first.lstrip(), "last": last, "house": row["house"]}
            students.append(student)

        #Another way to write this code so that you don't have to use list notation.. if you didnt need to split
        '''
        for name, house, in reader:
            students.append({"name": name, "house": house})
        '''

    #Write the second file
    with open(sys.argv[2], "w") as new_file:
        writer = csv.DictWriter(new_file, fieldnames = ["first", "last", "house"])
        writer.writeheader()
        writer.writerows(students)

if __name__ == "__main__":
    main()
