"""While Loops"""

__author__: str = "730652750"


def num_instances(phrase: str, search_char: str) -> int:
    index: int = 2
    count: bool = True
    while index < len(phrase):
        print(phrase[index])
        index = index + 1
        if index >= len(search_char):
            count = False
            return: int(index)


num_instances(phrase="HelloHeLloHEllo", search_char="e")
