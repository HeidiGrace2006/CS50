import random

#Loop for level
while True:
    try:
        level = input("Level: ")
        level = int(level)
        if level > 0:
            chosen_num = random.randint(1, level)
            break
        else:
            print("Please choose a positive integer.")
    except ValueError:
        pass

#Loop for guess
while True:
    try:
        guess = input("Guess: ")
        guess = int(guess)
        if guess > 0:
            if guess > chosen_num:
                print("Too large!")
            elif guess < chosen_num:
                print("Too small!")
            elif guess == chosen_num:
                print("Just right!")
                break
        else:
            print("Please choose a positive integer.")
    except ValueError:
        pass
