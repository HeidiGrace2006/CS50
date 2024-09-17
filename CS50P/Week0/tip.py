def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollarsNoSign = (d.replace("$", ""))
    return float(dollarsNoSign)


def percent_to_float(p):
    percentNoSign = (p.replace("%", ""))
    percentDec = float(percentNoSign) / 100
    return (percentDec)

main()