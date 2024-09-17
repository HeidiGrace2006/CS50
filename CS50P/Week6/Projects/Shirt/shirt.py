#Import
import sys
import os
from PIL import Image, ImageOps


def main():
    check_input()
    match_images()

#Check input (# of arg, type of ext, matching ext, existing)... (root + ext = path)
def check_input():
    first_path = os.path.splitext(sys.argv[1])
    second_path = os.path.splitext(sys.argv[2])

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif first_path[1] not in [".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"]:
        sys.exit("Invalid input file")
    elif second_path[1] not in [".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"]:
        sys.exit("Invalid output file")
    elif first_path[1] != second_path[1]:
        sys.exit("Input and output file extensions must match")
    try:
        open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input file does not exist.")


def match_images():
    #open shirt and get size
    shirt_file = Image.open("shirt.png")
    size = shirt_file.size

    #open image and resize
    image_file = Image.open(sys.argv[1])
    image_file = ImageOps.fit(image_file, size)

    #overlay 2 imgs
    with open(sys.argv[2], "w") as after:
        image_file.paste(shirt_file, shirt_file)
        image_file.save(sys.argv[2])

if __name__ == "__main__":
    main()
