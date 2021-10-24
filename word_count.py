"""
A program that counts the occurrances of a substring in a file given by the user

file: word_count.py

author: Donovan Griego

Date: 10-24-2021

assignment: Lab 9
"""


def count_words(contents, word="Foo"):
    """Returns the count of occurrances of a substring in a given string

    contents: The string to search
    word: The substring to count"""
    return contents.count(word)


def main():
    fname = input("Please enter a filename: ")
    word = input("Please enter a string to search for: ")
    try:
        with open(fname) as f:
            contents = f.read()
    except IsADirectoryError:
        print("Error; '{}' is a directory!".format(fname))
        exit(1)
    except FileNotFoundError:
        print("Error; file '{}' not found!".format(fname))
        exit(1)
    print("The string '{}' appears {} times in the file '{}'".format(
        word, count_words(contents, word), fname))


if __name__ == "__main__":
    main()
