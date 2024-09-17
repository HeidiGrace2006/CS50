import csv
import sys


def main():
    # TODO: Check for command-line usage
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a valid CSV file.")
    elif not sys.argv[2].endswith(".txt"):
        sys.exit("Not a valid text file.")
    else:
        try:
            open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("CSV file does not exist.")
        try:
            open(sys.argv[2])
        except FileNotFoundError:
            sys.exit("Text file does not exist.")

    # TODO: Read database file into a variable
    people = []
    with open(sys.argv[1], "r") as database_file:
        dict_reader = csv.DictReader(database_file)
        for row in dict_reader:
            people.append(row)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as sequence_file:
        sequence = sequence_file.read()

    # TODO: Find longest match of each STR in DNA sequence
    longest_counts = {}
    subsequences = list(people[0].keys())[1:]
    for subsequence in subsequences:
        longest_counts[subsequence] = longest_match(sequence, subsequence)

    # TODO: Check database for matching profiles
    for person in people:
        match = 0
        for subsequence in subsequences:
            if int(person[subsequence]) == longest_counts[subsequence]:
                match += 1

            if match == len(subsequences):
                print(person["name"])
                return
    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
