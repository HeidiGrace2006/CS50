import re

def main():
    html = input("HTML: ")
    print(parse(html))

def parse(html):
    if url := re.search(r"src=\"(https?://(?:www\.)?)(youtube\.com/embed)(/[a-zA-Z0-9]+)\"", html):
        https = url.group(1)
        yt = url.group(2)
        embed = url.group(3)

        https = ("https://")
        yt = ("youtu.be")

        return(f"{https}{yt}{embed}")
if __name__ == "__main__":
    main()

