#For packages... "pip". One ex.) is Cowsay. pip install cowsay
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])