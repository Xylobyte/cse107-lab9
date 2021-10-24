"""
A program that finds the differences between two files specified by the user

file: simplediff.py

author: Donovan Griego

Date: 10-24-2021

assignment: Lab 9
"""


def diff(string1, string2):
    """Prints the differences found in two difference string line by line.
    Compares each character and prints the differences along with a tag for location.

    string1: string 1 to compare
    string2: string 2 to compare"""
    # Split by new lines to get list of lines
    lines1 = string1.split("\n")
    lines2 = string2.split("\n")

    # Get max number of lines between the two
    most_lines = len(lines1) if len(lines1) > len(lines2) else len(lines2)

    # Pad each list by max number of lines to prevent Index out of bounds error
    lines1 += [''] * (most_lines - len(lines1))
    lines2 += [''] * (most_lines - len(lines2))
    print("")
    for i in range(most_lines):  # Check each line
        # Get max number of characters between the two lines
        most_characters = len(lines1[i]) if len(
            lines1[i]) > len(lines2[i]) else len(lines2[i])

        # Pad each line to the max number of characters to prevent index out of bounds error
        lines1[i] = lines1[i].ljust(most_characters)
        lines2[i] = lines2[i].ljust(most_characters)
        # Keep track of difference locations
        character_diffs = []
        for j in range(most_characters):    # Check each character
            # If a difference is found remember its location
            if lines1[i][j] != lines2[i][j]:
                character_diffs.append(j)
        # Create a string of length max_characters
        diff_string = " " * most_characters

        # Add a '^' at each difference location
        for d in character_diffs:
            diff_string = diff_string[:d] + "^" + diff_string[d + 1:]

        # If differences are found for this line print a tag with difference locations
        if len(character_diffs) > 0:
            print("{}c{}".format(
                i + 1, ",".join([str(e) for e in character_diffs])))

        # Print lines followed by diff_string to indicate location of differences visually
        print("> " + lines1[i])
        print("  " + diff_string)
        print("< " + lines2[i])
        print("  " + diff_string)
        if i != most_lines - 1:
            print("---")


def main():
    fname1 = input("Enter file name 1 >>> ")
    fname2 = input("Enter file name 2 >>> ")
    try:
        with open(fname1) as f:
            string1 = f.read()
    except IsADirectoryError:
        print("Error; '{}' is a directory!".format(fname1))
        exit(1)
    except FileNotFoundError:
        print("Error; file '{}' not found!".format(fname1))
        exit(1)

    try:
        with open(fname2) as f:
            string2 = f.read()
    except IsADirectoryError:
        print("Error; '{}' is a directory!".format(fname2))
        exit(1)
    except FileNotFoundError:
        print("Error; file '{}' not found!".format(fname2))
        exit(1)

    diff(string1, string2)


if __name__ == "__main__":
    main()
