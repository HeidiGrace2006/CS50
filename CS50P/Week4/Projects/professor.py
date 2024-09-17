import random

def main():
    level = get_level()
    score = run_game(level)
    print("Score: ", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                break
            else:
                print("Please choose level 1, 2, or 3.")
        except ValueError:
            print("Please choose level 1, 2, or 3.")
    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y

def one_round(x, y):
    tries = 0
    while tries < 3:
        try:
            user_answer = int(input(f"{x} + {y} = "))
            if user_answer == (x + y):
                return True
            else:
                tries += 1
                print("EEE")
        except ValueError:
            tries += 1
            print("EEE")
    if tries == 3:
        print(f"{x} + {y} = {(x+y)}")
        print("-----------")
        return False

def run_game(level):
    i = 0
    score = 0
    while i < 10:
        x, y = generate_integer(level)
        if one_round(x, y) == True:
            score += 1
        i += 1
    return score

if __name__ == "__main__":
    main()