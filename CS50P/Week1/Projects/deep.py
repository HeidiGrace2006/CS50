question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
question = question.strip().replace("-", " ").lower()

if question == "42" or question == "forty two":
    print("Yes")
else:
    print("No")
