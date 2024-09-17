import re
email = input("What's your email? ").strip()

#Searching email for the right characters
if re.search(r"^(\w|\.)+@(\w+\.)?\w.+\.(com|edu|net|gov|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

'''

re.search(pattern, string, flags=0)

.   any character except a new line
*   0 or more repetitions
+   1 or more repetitions
?   0 or 1 repetition
{m} m repetitions
{m,n} m-n repetitions

^   matches the start of the string
$   matches the end of the string or just before the newline at the end of the string

[]    set of characters
[^]   complementing the set .. means any character EXCEPT what comes after ^

\d    decimal digit
\D    not a decimal digit
\s    whitespace characters
\S    not a whitespace character
\w    word character, as well as numbers and the underscore
\W    not a word character

(...) captures
(?:...) to escape capture

'''