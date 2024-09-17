
while True:
    try:
        height = int(input("height: "))
        if 0 < height <= 8:
            break
    except ValueError:
        pass


row = 0
while row < height:
    spaces = 0
    while spaces < height - row - 1:
        print(" ", end="")
        spaces += 1
    i = 0
    while i <= row:
        print("#", end="")
        i += 1
    print("  ", end="")
    j = 0
    while j <= row:
        print("#", end="")
        j += 1
    print()
    row += 1
