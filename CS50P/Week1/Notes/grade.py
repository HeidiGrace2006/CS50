#Ask for grade
score = int(input("Enter score: "))

#Assign grade value
if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 61 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")