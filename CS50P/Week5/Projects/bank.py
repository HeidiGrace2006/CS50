def main():
    greeting = input("Greet me! ")
    print (value(greeting))

def value(greeting):
    if "hello" in greeting.lower():
        return(0)
    elif "h" == greeting[0].lower():
        return(20)
    else:
        return(100)

if __name__ == "__main__":
    main()