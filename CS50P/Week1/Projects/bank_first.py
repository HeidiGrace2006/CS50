
greeting = input("Greet me! ")
greeting = greeting.lower().strip()

if "hello" in greeting:
    print("$0")
elif "h" == greeting[0]:
    print("$20")
else:
    print("$100")