# Get text and count
text = input("Text: ")
letters, words, sentences, i = 0, 1, 0, 0

for i in range(len(text)):
    if text[i].isalpha():
        letters += 1
    elif text[i] == " ":
        words += 1
    elif text[i] == "." or text[i] == "!" or text[i] == "?":
        sentences += 1

# Calculate
L = float((letters) / (words)) * 100
S = float((sentences) / (words)) * 100
grade = round(0.0588 * L - 0.296 * S - 15.8)

# Print grade
if grade > 16:
    print("Grade 16+")
elif grade < 1:
    print("Before Grade 1")
else:
    print(f"Grade", grade)
