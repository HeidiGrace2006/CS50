#input expression as string
expression = input("Expression: ")

#split string
x, y, z = expression.split(" ")

#convert string to float
x = float(x)
z = float(z)

#calculte, round, and print
if y == "+":
    answer = (x + z)
    print(round(answer, 1))
elif y == "-":
    answer = (x - z)
    print(round(answer, 1))
elif y == "*":
    answer = (x * z)
    print(round(answer, 1))
elif y == "/":
    answer = (x / z)
    print(round(answer, 1))
else:
    print("Invalid expression.")
