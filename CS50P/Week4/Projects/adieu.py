import inflect

names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        p = inflect.engine()
        names = p.join(names)
        print()
        print("Adieu, adieu, to", names)
        break