def main():

    #ask for a time
    response = input("Time: ")
    #call converted time function
    time = convert(response)

    #print breakfast lunch or dinner
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):

    #convert string given (time) to float
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)

    minCorrect = minutes/60

    time = hours + minCorrect

    return time

if __name__ == "__main__":
    main()
'''
    #if len(time) = 4.. insert 0 to [0]
    if len(time) == 4:
        time.insert(0, 0)
'''