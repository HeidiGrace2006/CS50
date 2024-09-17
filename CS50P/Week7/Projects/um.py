import re

def main():
    sentence = input("Text: ").lower()
    print(count(sentence))

def count(sentence):
    ums = re.findall(r"\b(um)\b", sentence, re.IGNORECASE)
    return len(ums)

if __name__ == "__main__":
    main()
