import glob
import re
import zipfile

import requests
from tomlkit import integer

nothing_var = "90052"
text = ".txt"
list_files = []
list_comments = []

with zipfile.ZipFile("src/ZipChallenge6/channel.zip") as file:
    count = len(file.infolist()) - 1
    for var1 in range(count):
        list_comments.append(file.getinfo(str(nothing_var) + ".txt").comment)
        with file.open(str(nothing_var) + ".txt") as archive:
            for line in archive:
                if re.search("\d+", str(line)):
                    nothing_var = re.findall("\d+", str(line))
                    nothing_var = "".join(nothing_var)
                    list_files.append(nothing_var)
                else:
                    print(line)

list_comments = list(map(str, list_comments))

print("".join(list_comments))


def main():
    print("hiho")

    base_folder = "src/ZipChallenge6/channel/"
    seed = "90052"

    with open(base_folder + seed + ".txt") as f:
        text = f.read()
    print(text)
    base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

    while text.split(" ")[-1].isnumeric():

        new_num = text.split(" ")[-1]
        with open(base_folder + new_num + ".txt") as f:
            text = f.read()

        print(requests.get(base_url + new_num).text)

        # print(text)


def searchForComments():
    all_text_files = glob.glob("src/ZipChallenge6/channel/*.txt")
    for file in all_text_files:
        with open(file) as f:

            file.getinfo(str(nothing_var) + ".txt").comment
            text = f.read()

        if len(text.split(" ")) != 4:
            print(file)
            print(text)

        # if "Next nothing is" not in text:
        #     print(file)
        #     print(text)


def urlRequests():
    base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    # seed = "12345"
    # seed (divide by 2 )= "16044"
    seed = "46145"
    text_in_page = requests.get(base_url + seed).text
    print(text_in_page)

    while text_in_page.split(" ")[-1].isnumeric():
        new_num = text_in_page.split(" ")[-1]
        text_in_page = requests.get(base_url + new_num).text
        print(text_in_page)


def tryReadZip():
    import zipfile

    with zipfile.ZipFile("src/ZipChallenge6/channel.zip", "r") as zip_ref:
        zip_ref.extractall("src/ZipChallenge6/channel")


if __name__ == "__main__":
    # main()
    # searchForComments()
    urlRequests()
