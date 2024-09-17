import validators
response = input("Email: ")
if validators.email(response) == True:
    print("Valid")
else:
    print("Invalid")
