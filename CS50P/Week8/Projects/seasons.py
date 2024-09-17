from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    birthday = input("Date of birth 'YYYY-MM-DD': ")
    print (check(birthday), "minutes")

def check(birthday):
    try:
        difference = date.today() - date.fromisoformat(birthday)
    except:
        sys.exit("Invalid date")
    minutes = (difference.days * 24 * 60)
    return p.number_to_words(minutes, andword="").capitalize()


if __name__ == "__main__":
    main()

'''
class Calculate:
    #initalize variable
    def __init__(self, years, months, days):
        self.years = years
        self.months = months
        self.days = days

    #overload sub
    def __sub__(self, other):
        years = self.years - other.years
        months = self.months - other.months
        days = self.days - other.days
'''