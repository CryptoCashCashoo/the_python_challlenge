# from urllib import request
import pickle


def main():

    with open("src/banner.pkl", "rb") as f:
        data = pickle.load(f)

    decyphered = ""
    for list in data:
        for character, count in list:
            for i in range(count):
                decyphered += character
        decyphered += "\n"
    print(decyphered)


if __name__ == "__main__":
    main()
