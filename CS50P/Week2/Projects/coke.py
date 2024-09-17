
#create due = 50
due = 50

while due > 0:
    #output Amount Due
    print("Amount Due:", due)

    #have the user input coin
    coin = int(input("Input Coin: "))

    #subtract coin from amount due.. re output
    if coin == 25 or coin == 10 or coin == 5:
        due = due - coin
    else:
        print("Amount Due:", due)

#if amount due <= 0 .. output change due
change = abs(due)
print("Change Owed:", change)

