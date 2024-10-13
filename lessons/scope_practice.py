"""Some scope examples."""


def remove_chars(msg: str, char: str) -> str:
    copy: str = ""  # set up empty string and then we can copy values over
    index: int = 0
    while index < len(msg):
        # if the letter is NOT char
        if msg[index] != char:
            # add it to copy
            copy = copy + msg[index]
        index += 1
    return copy


if __name__ == "__main__":
    # create a variable called word with the values "yoyo"
    word: str = "yoyo"  # GLOBAL varible
    # print the result of calling your function with the argumrnts word and "y"
    print(
        remove_chars(word, "y")
    )  # word and y are positional arguments, so they are the arguments assigned to the parameters for msg and char from og code
# print the result of calling your function with arguments and "o"
# print(remove_chars(word, "o"))
