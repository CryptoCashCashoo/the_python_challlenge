# from urllib import request
import requests


def main():
    base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    # seed = "12345"
    # seed (divide by 2 )= "16044"
    seed = "16780"
    text_in_page = requests.get(base_url + seed).text
    print(text_in_page)

    while text_in_page.split(" ")[-1].isnumeric():
        new_num = text_in_page.split(" ")[-1]
        text_in_page = requests.get(base_url + new_num).text
        print(text_in_page)

if __name__ == "__main__":
    main()
