import requests
import sys

#try and except to confirm proper input
try:
    if len(sys.argv) == 2:
        n = float(sys.argv[1])
    elif len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Please enter ONE command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

#try and except to get and convert website
try:
    #Get the website from bit coins api using requests
    website = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    #convert the website info into a dictionary using json
    website_dict = website.json()
#Exception for in case the website doesnt work/goes down
except requests.RequestException:
    sys.exit("Request exception error")

#access the dictionary created by going through the list of keys.. multiply for total cost
total = (website_dict["bpi"]["USD"]["rate_float"] * n)
#format for thousands separation, and round to 4 places
print(f"${total:,.4f}")