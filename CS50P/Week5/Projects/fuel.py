def main():
    fraction = input("Fraction: ")
    percent = convert(fraction)
    result = gauge(percent)
    print(result)

def convert(fraction):
    while True:
        try:
            x, y = (fraction.split("/"))
            fraction = (int(x)/int(y))
            if fraction <= 1:
                percent = round(fraction * 100)
                return percent
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise
def gauge(percent):
    if percent >= 0 and percent <= 1:
        return "E"
    elif percent >= 99 and percent <= 100:
        return "F"
    else:
        return str(f"{percent}%")

if __name__ == "__main__":
    main()