def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if s [0:2].isalpha() == False:
        return False
    elif s.isalnum() == False:
        return False
    elif 2 > len(s) or len(s) > 6:
        return False

    digit_count = 0
    for char in s:
        if char.isdigit():
            digit_count += 1
            if char == "0" and digit_count == 1:
                return False
        if char.isalpha() and digit_count > 0:
            return False
    else:
        return True

if __name__ == "__main__":
    main()
