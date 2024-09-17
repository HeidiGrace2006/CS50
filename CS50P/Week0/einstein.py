def main():
    print("E = mc². Please enter m to solve.")
    mass = int(input("m: "))

    energy = round(mass * (300000000 ** 2))
    print(f"E = {energy:,} Joules")

main()