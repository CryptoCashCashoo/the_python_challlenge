""" MAIN """
from collections import Counter
from curses.ascii import islower


def main() -> None:

    crypted = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

    decyphered = ""
    for c in crypted:
        if c == " ":
            decyphered += c
            continue
        if not (ord(c) >= 97 and ord(c) <= 122):
            decyphered += c
            continue
        newC = chr(((ord(c) + 2 - 97) % 26) + 97)
        decyphered += newC

    # print(decyphered)
    """i hope you didnt translate it by hand. 
    thats what computers are for. 
    doing it in by hand is inefficient and that's why this text is so long. 
    using string.maketrans() is recommended. now apply on the url."""


def CountRareCharacters() -> None:
    with open("src/RareText.txt") as f:
        text = f.read()

    print(Counter(text))


def show_lower_case_letters_surrounded_by_3_upper_case() -> None:
    with open("src/Challenge3.txt") as f:
        text = f.read()

    # print(text);

    decypher = ""
    for i, c in enumerate(text):
        if i < 4 or i > len(text) - 5:
            continue

        if c.islower():
            if (
                text[i - 4].islower()
                and text[i - 3].isupper()
                and text[i - 2].isupper()
                and text[i - 1].isupper()
                and text[i + 1].isupper()
                and text[i + 2].isupper()
                and text[i + 3].isupper()
                and text[i + 4].islower()
            ):
                    decypher += c
    print(decypher)


if __name__ == "__main__":
    show_lower_case_letters_surrounded_by_3_upper_case()
