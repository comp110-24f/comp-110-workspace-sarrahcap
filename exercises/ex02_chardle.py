"""EX02 - Chardle - Build your own Wordle."""

__author__ = "730652750"


def input_word() -> str:
    q_word = input(
        "Enter a 5-character word: "
    )  # input() prompts code to ask user whats in ()
    if len(q_word) == 5:
        print(q_word)
    else:
        print("Error: Word must contain 5 characters. ")
        exit()
    return q_word


def input_letter() -> str:
    q_letter = input("Enter a single character: ")
    if len(q_letter) == 1:  # will only accecpt single letters
        print(q_letter)
    else:
        print("Error: Character must be a single character.")
        exit()  # exits function
    return q_letter


def contains_char(word: str, letter: str) -> None:
    print("Searching for {letter} in {word}")
    count = 0
    for contains_char in word:
        if contains_char == letter:
            count += 1  # if count = letter, count increases by 1
            print("The letter {letter} appears {count} times in the word {word}.")
        else:
            print("No instances of{letter} found in {word}")


def main() -> None:  # defining contains_char parameters
    word = input_word()
    letter = input_letter()
    contains_char(word, letter)


if __name__ == "__main":
    main()
