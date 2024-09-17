# Get cents
while True:
    try:
        cents = float(input("Cents: "))
        if cents > 0:
            break
    except ValueError:
        pass

# Multiply cents
cents = round(cents * 100)

# Quarters
quarters = 0
while cents >= 25:
    cents -= 25
    quarters += 1

# Dimes
dimes = 0
while cents >= 10:
    cents -= 10
    dimes += 1

# Nickles
nickles = 0
while cents >= 5:
    cents -= 5
    nickles += 1

# Pennies
pennies = 0
while cents >= 1:
    cents -= 1
    pennies += 1

# Print
print(quarters + dimes + nickles + pennies)
