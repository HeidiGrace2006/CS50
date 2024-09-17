import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    chosen_font = random.choice(fonts)
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        if sys.argv[2] in fonts:
            chosen_font = sys.argv[2]
        else:
            sys.exit("invalid font.")
else:
    sys.exit("incorrect number of arguments.")

text = input("Input: ")
figlet.setFont(font = chosen_font)
print("Output: \n", figlet.renderText(text))


