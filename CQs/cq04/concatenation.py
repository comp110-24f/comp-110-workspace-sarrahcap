"""Importing CQ - concatenation."""

__author__ = "730652750"


def concat(param1, param2) -> str:
    return param1 + param2


word1 = "happy"
word2 = "tuesday"

if __name__ == "__main__":
    concatenation = concat(word1, word2)
    print(concatenation)
