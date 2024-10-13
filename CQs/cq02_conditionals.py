"""Guessing game."""

__author__: str = "730652750"


def guess_a_number() -> None:
    y: int = int(input("Guess a number:"))
    secret = int(7)
    print("Your guess was " + str(y))

    if y == secret:
        print("You got it!")
    elif y < 7:
        print("Your guess was too low! The secret number is 7.")
    else:
        print("Your guess was too high! The secret number is 7.")


if __name__ == "__main__":
    guess_a_number()
