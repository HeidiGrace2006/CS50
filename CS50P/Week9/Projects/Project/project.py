import random, time, sys

def main():
    if not previously_played():
        game_tutorial()
    category = get_category()
    word = get_word(category)
    if gameplay(word) == True:
        print_slow("You win!")
        fireworks()
    else:
        print_slow("You lose!")
        print(f"The word was {word}.")

#Dict with list of categories
categories = {
    "plants" : ["cactus", "basil", "lettuce", "lavender", "orchid", "hibiscus", "flower", "thyme", "herb"],
    "animals": ["salamander", "ostrich", "reindeer", "kangaroo", "butterfly", "rooster", "lizard", "skate", "pheasant", "partridge", "moose", "cougar", "wolf", "elephant", "giraffe", "tiger"],
    "music": ["treble", "bass", "octave", "cadence", "trill", "soprano", "vivace", "dolce", "molto", "cadenza", "mozart", "jazz", "rock", "classical", "folk"],
    "biology": ["organism", "mitochondria", "life", "chromosome", "bacteria", "organ", "nucleus", "cytoplasm"],
    "desserts": ["icecream", "tiramisu", "cupcake", "mousse", "custard", "cheesecake", "danish", "donut", "cookie", "brownie"],
    #option for all
}
icecream_cone = [
    "       ()",
    "      (__)",
    "     (____)",
    "    (______)",
    "   (________)",
    "  (__________)",
    r"   \/\/\/\/\/",
    r"    \/\/\/\/",
    r"     \/\/\/",
    r"      \/\/",
    r"       \/"
]

def fireworks():
    print(r"                                   .''.       ")
    print(r"       .''.      .        *''*    :_\/_:     . ")
    print(r"      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.")
    print(r"  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-")
    print(r" :_\/_:'.:::.    ' *''*    * '.\ /.' _\(/_'.':'.'")
    print(r" : /\ : :::::     *_\/_*     -= o =-  /)\    '  *")
    print(r"  '..'  ':::'     * /\ *     .'/.\'.   '")
    print(r"      *            *..*         :")

#find out if you should run the tutorial (have they played before)
def previously_played():
    print_slow("\nWelcome to Icecream Inquiry! The less-gruesome version of hangman.")
    while True:
        print_slow("Have you played before? [yes/no]")
        played = input("").lower()
        if played == "yes":
            print_slow("Then lets begin!")
            return True
        elif played == "no":
            print_slow("Alright, I'll teach you.")
            return False

#Get input
def get_category():
    while True:
        print("\nSelect a category:", end="")
        #print list
        print("   ",*categories.keys(), "all", sep="\n   ")
        category = input("Selection: ").lower()
        #Check input
        if category in categories.keys() or category == "all":
            break
        elif category not in categories.keys() and category != "all":
            print_slow("\nThat is not a valid category.")
    return category

#When category selected.. pick a random word from that category and set it as the special_word
def get_word(category):
    #if 'all' is selected:
    if category == "all":
        words = [random.choice(categories[key]) for key in categories]
        word = random.choice(words)
    #Else:
    else:
        word = random.choice(categories[category])
    return word

#if previously_played == False.. game tutorial.
def game_tutorial():
    print_slow("Here is my icecream cone: ")
    print(*icecream_cone, sep="\n")
    print_slow("Your goal is to guess the word I'm thinking of before I finish my icecream cone. \n(That means you can guess incorrectly 10 times!)\n")
    print_slow("I'll even let you pick the category of the word.\nOnce I've choosen a word from the category you'd like, you can guess which letters are in the word (one at a time.)\n")
    print_slow("If you guess correctly, I'll show you where the letter appears in the word. But if you're wrong, I get to eat a layer of icecream!")
    print_slow("Enough talking. Let's start!")


guessed_letters = []
guessed_correct = []
#the 'main' of of the game
def gameplay(word):
    while True:
        status(word)
        guess = guessing()
        if guess in word:
            if win_check(guess, word) == True:
                return True
        elif guess not in word:
            if lose_check() == True:
                return False

def status(word):
    #print what letters have been guessed
    if len(guessed_letters) != 0:
        print_slow("\nSo far you have guessed: ")
        print(*guessed_letters, sep=", ")

    #print what they have of the word
    print("The word is: \n")
    for letter in word:
        if letter in guessed_letters:
            print(letter, end="")
        else:
            print("_ ", end="")

def guessing():
    while True:
        guess = input("\n\nGuess a letter: ")
        guess = guess.lower()
        #checking input
        if guess.isalpha() == False:
            print("I told you to guess a letter!")
        elif guess in guessed_letters:
            print("You have already guessed that letter.")
        else:
            guessed_letters.append(guess)
        return guess

#guessed right
def win_check(guess, word):
    guessed_correct.append(guess)
    print_slow("Yep!\n")
    #using all and a 'generator expression'
    #checks if all letters in the 'word' are in guessed_correct
    if all(letter in guessed_correct for letter in word):
        return True
    else:
        return False

#guessed wrong
def lose_check():
    print_slow("Nope!\n")
    icecream_cone.remove(icecream_cone[0])
    print(*icecream_cone, sep="\n")
    if len(icecream_cone) == 1:
        print("You can't make anymore wrong guesses, or you lose!")
    #if icecream cone is finished.. they lose
    elif len(icecream_cone) == 0:
        return True
    else:
        print(f"You can only make {(len(icecream_cone))-1} more wrong guesses.")
        return False

#to simulate actual typing from a person
def print_slow(str):
    for char in str + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != "\n":
            time.sleep(0.05)
        else:
            time.sleep(0.3)

if __name__ == "__main__":
    main()

