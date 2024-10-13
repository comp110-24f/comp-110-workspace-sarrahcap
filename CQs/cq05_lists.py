"""Mutating functions."""

__author__ = "730652750"


def manual_append(list1: list[int], value: int) -> None:
    list1.append(value)


def double(list2: list[int]) -> None:
    index: int = 0

    while index < len(list2):
        list2[index] *= 2
    index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
