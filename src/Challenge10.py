"http://www.pythonchallenge.com/pc/return/bull.html"


def look_and_say_seq():
    iter = "1"
    yield iter

    while True:
        nextValue = ""
        curr_char = None
        for c in iter:
            if curr_char is None:
                curr_char = c
                count = 1
            elif curr_char != c:
                nextValue += str(count) + curr_char
                curr_char = c
                count = 1
            else:
                count += 1
        nextValue += str(count) + curr_char

        iter = nextValue

        yield iter


def main():
    seq = look_and_say_seq()

    look_and_say = [next(seq) for _ in range(31)]
    len(look_and_say)
    print(len(look_and_say[30]))


if __name__ == "__main__":
    main()
