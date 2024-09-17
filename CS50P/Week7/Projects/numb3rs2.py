import re

def main():
    ip = input("IPv4 Address: ")
    print(validate(ip))

def validate(ip):
    if matches := re.fullmatch(r"([0-9^-]{0,3})\.([0-9^-]{0,3})\.([0-9^-]{0,3})\.([0-9^-]{0,3})", ip):
        set1 = matches.group(1)
        set2 = matches.group(2)
        set3 = matches.group(3)
        set4 = matches.group(4)
    else:
        return False
    try:
        if 0<= int(set1) <= 225 and 0<= int(set2) <= 225 and 0<= int(set3) <= 225 and 0<= int(set4) <= 225:
            return True
        else:
            return False
    except ValueError:
        return False

if __name__ == "__main__":
    main()