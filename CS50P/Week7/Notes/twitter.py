import re

url = input("URL: ").strip()

matches = re.search(r"^https?://(www\.)?twitter\.com/([a-z0-9_])$", url, re.IGNORECASE)
if matches:
    #Group 2 bc the parenthases around "www" basically "captures" it as a group
    #syntax: (...) captures, (?:...) doesnt
    print(f"Username:", matches.group(2))

'''
#re.sub(pattern, repl, string, count=0, flags=0)
username re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")

#username = url.removeprefix("https://twitter.com/", "")
'''