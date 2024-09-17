import re

def main():
    initial_hours = input("Hours: ")
    print(convert(initial_hours))

def convert(initial_hours):
    #Search for format and then group
    if time := re.search(r"^([0-9]+):?([0-5][0-9])? (AM|PM) to ([0-9]+):?([0-5][0-9])? (AM|PM)$", initial_hours):
        bgn_hr = time.group(1)
        bgn_min = time.group(2)
        first_meridiem = time.group(3)
        end_hr = time.group(4)
        end_min = time.group(5)
        second_meridiem = time.group(6)

        #Converting the hours
        if first_meridiem == "PM" and bgn_hr != "12":
            new_bgn_hr = int(bgn_hr) + 12
        if first_meridiem == "PM" and bgn_hr == "12":
            new_bgn_hr = bgn_hr
        if first_meridiem == "AM" and int(bgn_hr) < 10:
            new_bgn_hr = (f"{0:01}{bgn_hr}")
        if first_meridiem == "AM" and bgn_hr == "12":
            new_bgn_hr = "00"
        if second_meridiem == "PM" and end_hr != "12":
            new_end_hr = int(end_hr) + 12
        if second_meridiem == "PM" and end_hr == "12":
            new_end_hr = end_hr
        if second_meridiem == "AM" and end_hr == "12":
            new_end_hr = "00"
        if second_meridiem == "AM" and int(bgn_hr) < 10:
            new_end_hr = (f"{0:01}{end_hr}")

        #Checking the minutes and returning
        if bgn_min:
            return(f"{new_bgn_hr}:{bgn_min} to {new_end_hr}:{end_min}")
        else:
            return(f"{new_bgn_hr}:00 to {new_end_hr}:00")
    else:
        raise ValueError


if __name__ == "__main__":
    main()

#Original code works, but messier:
'''
def convert(initial_hours):
    #Dictionaries with conversions
    AM = {
        "12":"00",
        "1":"01",
        "2":"02",
        "3":"03",
        "4":"04",
        "5":"05",
        "6":"06",
        "7":"07",
        "8":"08",
        "9":"09",
        "10":"10",
        "11":"11"}
    PM = {
        "12":"12",
        "1":"13",
        "2":"14",
        "3":"15",
        "4":"16",
        "5":"17",
        "6":"18",
        "7":"19",
        "8":"20",
        "9":"21",
        "10":"22",
        "11":"23"}


        #Search for the first format option, and group the conponents
    if format_one := re.search(r"^([0-9]+):([0-9]+) (AM|PM) to ([0-9]+):([0-9]+) (AM|PM)$", initial_hours):

        bgn_hrs = format_one.group(1)
        bgn_min = format_one.group(2)
        first_meridiem = format_one.group(3)
        end_hrs = format_one.group(4)
        end_min = format_one.group(5)
        second_meridiem = format_one.group(6)

        #Removing 0's bc python doesnt like "01" (etc)
        if bgn_min.startswith("0") and bgn_min != "00":
            bgn_min = bgn_min.replace("0", "")
        if end_min.startswith("0") and end_min != "00":
            end_min = end_min.replace("0", "")

        #Checking that input was actual times.. and if so, converting the time
        if 1<= int(bgn_hrs) <=12 and 1<= int(end_hrs) <=12 and 0<= int(bgn_min) <=59 and 0<= int(end_min) <=59:
            if first_meridiem == "AM":
                for key in AM:
                    if key == bgn_hrs:
                        bgn_hrs = AM[bgn_hrs]
            elif first_meridiem == "PM":
                for key in PM:
                    if key == bgn_hrs:
                        bgn_hrs = PM[bgn_hrs]
            if second_meridiem == "AM":
                for key in AM:
                    if key == end_hrs:
                        end_hrs = AM[end_hrs]
            elif second_meridiem == "PM":
                for key in PM:
                    if key == end_hrs:
                        end_hrs = PM[end_hrs]
            if len(str(bgn_min)) == 1:
                bgn_min = (f"{0:01}" + bgn_min)
            if len(str(end_min)) == 1:
                end_min = (f"{0:01}" + end_min)
            return(f"{bgn_hrs}:{bgn_min} to {end_hrs}:{end_min}")
        else:
            raise ValueError


    #Search for the second format option, and group the conponents
    elif format_two := re.search(r"^([0-9]+) (AM|PM) to ([0-9]+) (AM|PM)$", initial_hours):
            bgn_hr = format_two.group(1)
            bgn_meridiem = format_two.group(2)
            end_hr = format_two.group(3)
            end_meridiem = format_two.group(4)

            #Checking that input was actual times.. and if so, converting the time
            if 1<= int(bgn_hr) <=12 and 1<= int(end_hr) <=12:
                if bgn_meridiem == "AM":
                    for key in AM:
                        if key == bgn_hr:
                            bgn_hr = AM[bgn_hr]
                elif bgn_meridiem == "PM":
                    for key in PM:
                        if key == bgn_hr:
                            bgn_hr = PM[bgn_hr]
                if end_meridiem == "AM":
                    for key in AM:
                        if key == end_hr:
                            end_hr = AM[end_hr]
                elif end_meridiem == "PM":
                    for key in PM:
                        if key == end_hr:
                            end_hr = PM[end_hr]
                min = ":00"
                return(f"{bgn_hr}{min} to {end_hr}{min}")
            else:
                raise ValueError
'''
