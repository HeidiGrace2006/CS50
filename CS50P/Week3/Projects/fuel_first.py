while True:
    #prompt for fraction
    fraction = input("Fraction: ")

    try:
        #separate and store as ints as x and y
        x, y = (fraction.split("/"))
        if y == 0:
            pass
        else:
            #create percent
            percent = round((int(x)/int(y)) * 100)
            if percent > 100:
                pass
            else:
                break
    except (ValueError, ZeroDivisionError):
        pass

#if percent.. F, E (string)
if percent >= 0 and percent <= 1:
    print("E")
elif percent >= 99 and percent <= 100:
    print("F")
else:
    print(f"{percent}%")

