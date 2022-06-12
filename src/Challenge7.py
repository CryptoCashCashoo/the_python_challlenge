"""http://www.pythonchallenge.com/pc/def/oxygen.html"""
from collections import Counter

from PIL import Image


def main():
    im = Image.open("src/Challenge7/oxygen.png")

    vcenter = im.height / 2
    color_list = [im.getpixel((x, vcenter)) for x in range(0, im.width, 7)][:-3]
    print(color_list)

    decyphered = ""
    for col in color_list:
        decyphered += chr(col[0])
    print(decyphered) # smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]

    order_character_solution = [105, 110, 116, 101, 103, 114, 105, 116, 121]
    print( "".join([chr(x) for x in order_character_solution]))
    

# decyphered = ""
# for col in color_list:
#     if col[0] in translator:
#         decyphered += translator[col[0]]
#     else:
#         decyphered += f"{col[0]}"
# print(decyphered)

if __name__ == "__main__":
    main()
