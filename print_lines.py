def print_stars_line_length_ten():
    print("*"*10)


def print_stars_line(length):
    print(length*"*")


def print_line(length, character):
    print(character*length)


def main():
    line_length = 25

    print_stars_line_length_ten()
    print_stars_line(line_length)
    print_stars_line(line_length + 5)

    char = '#'
    print_line(line_length, character="%")
    print_line(length=line_length, character=char)


if __name__ == "__main__":
    main()