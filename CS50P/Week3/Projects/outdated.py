
months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

broken = 0
while True:
    try:
        inital_date = input("Date: ").title().strip()

        if "/" in inital_date:
            month, day, year = inital_date.split("/")
            if month.isalpha() or int(month) > 12 or int(day) > 31:
                broken += 1
            else:
                break
        elif "," in inital_date:
            month, day, year = inital_date.split(" ")
            day = day.replace(",", "")
            if month.isnumeric() or int(day) > 31:
                broken += 1
            else:
                break
    except broken > 0:
        pass
    except:
        pass

if broken == 0:
    if len(day) == 1:
        day = "0" + day
    else:
        day = day

    if month in months:
        print(f"{year}-{months[month]}-{day}")
    else:
        if len(month) == 1:
            month = "0" + month
        else:
            month = month
        print(f"{year}-{month}-{day}")
