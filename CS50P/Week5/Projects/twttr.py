def main():
    response = input("Input: ")
    print(shorten(response))

def shorten(response):
    new_word = ""
    for char in response:
        if char.lower() not in "aeiou":
            new_word += char
    return new_word

if __name__ == "__main__":
    main()