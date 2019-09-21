from cs50 import get_string
from sys import argv


def main():

    # TODO
    if len(argv) != 2:
        print("Usage: python bleep.py dictionary")
        exit(1)

    file = open(argv[1], "r")
    banned_words = set()
    for line in file:
        banned_words.add(line.strip().lower())
    input_string = get_string("What message would you like to censor?\n")
    output_string = ""
    words = input_string.split()

    for word in words:
        if word.lower() in banned_words:
            output_string += "*" * len(word) + " "
        else:
            output_string += word + " "
    print(output_string.strip())

# main function
if __name__ == "__main__":
    main()