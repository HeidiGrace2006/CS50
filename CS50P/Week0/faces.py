def main():
    text = input("Please enter a smiley or frownie face ")
    conversion = convert(text)
    print(conversion)

def convert(text):
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    return text

main()