def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #Check: 1st two dig are alpha
    if s [0:2].isalpha() == False:
        return False
    #Check: no special char
    elif s.isalnum() == False:
        return False
    #Check: length
    elif 2 > len(s) or len(s) > 6:
        return False

    #create digit count
    digit_count = 0
    #every time a digit is used, +1
    for char in s:
        if char.isdigit():
            digit_count += 1
            #check that 1st num isnt 0
            if char == "0" and digit_count == 1:
                return False
        #if digit count > 0 and char is alpha..false
        if char.isalpha() and digit_count > 0:
            return False
    else:
        return True

main()
