import re

def main():
    ip = input("IPv4 Address: ")
    print(validate(ip))

def validate(ip):
    if matches := re.fullmatch(r"([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)", ip):
        set1 = matches.group(1)
        set2 = matches.group(2)
        set3 = matches.group(3)
        set4 = matches.group(4)
    else:
        return False
    try:
        if 0<= int(set1) <= 255 and 0<= int(set2) <= 255 and 0<= int(set3) <= 255 and 0<= int(set4) <= 255:
            return True
        else:
            return False
    except ValueError:
        return False

if __name__ == "__main__":
    main()