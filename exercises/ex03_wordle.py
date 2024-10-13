"""DIY Wordle!"""

__author__ = "730652750"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def input_guess(secret_word_len: int) -> str:
    """determine length of secret word & user guess"""
    while True:
        #input causes function to prompt user for word
        guess = input(f"Enter a {secret_word_len} character word: ")
        #if length of the users input is correct, return user input
        if len(guess) == secret_word_len:
            return guess
        #if not, prompt user to retry
        else:
            print(f"That wasn't {secret_word_len} chars! Try again: ")


def contains_char(secret_word: str, char_guess: str) -> bool:
    """determine if letter guess is inside word"""
    assert len(char_guess) == 1
    #if letter is in word
    if char_guess in secret_word:
        #write true
        return True
    else:
        #if not, write false
        return False


def emojified(user_guess: str, secret_word1: str) -> str:
    assert len(user_guess) == len(secret_word1)
    index: int = 0
    while user_guess in secret_word1:
        if secret_word1[index] == user_guess:

