"""Find and remove max value"""

__author__ = "730652750"


def find_and_remove_max(list: list[int]) -> int:
    max_value = max(list)
    if len(list) == 0:
        return -1
    while max_value in list:
        idx: int = list.index(max_value)
        list.pop(idx)

    return max_value
