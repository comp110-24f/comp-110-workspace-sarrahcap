"""Guessing game."""

__author__: str = "730652750"


def guess_a_number() -> None:
    y = input("Guess a number:")
    x = 7
    print("Your guess was " + y)

    if y == str(7):
        print("You got it!")
    elif y < str(7):
        print("Your guess was too low! The secret number is " + str(x))
    else:
        print("Your guess was too high! The secret number is " + str(x))


if __name__ == "__main__":
    guess_a_number()
