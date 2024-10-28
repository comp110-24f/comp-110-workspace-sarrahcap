"""Implementing list utility functions."""

__author__ = "730652750"


def only_evens(int_list: list[int]) -> list[int]:
    even_num = []  # define new argument so original list is not mutated
    for elem in int_list:
        if (
            elem % 2 == 0
        ):  # when the remainder of dividing a # from list by 2 is 0 (aka # is even),
            even_num.append(elem)  # add # to new argument list
    return even_num  # return the new list of only even #'s


def sub(range_list: list[int], start_idx: int, end_idx: int) -> list[int]:
    if len(range_list) == 0:
        return []  # if range_list has no values, return []
    if start_idx >= len(range_list):
        return []  # if start is greater or equal to length of list, return []
    if end_idx <= 0:
        return []  # if end is less or equal to length of list, return []
    if start_idx < 0:  # if start is negative
        start_idx = 0  # start becomes 0
    if end_idx > len(range_list):  # if end is larger than length of list
        end_idx = len(range_list)  # end becomes length of list
    new_list = [range_list[elem] for elem in range(start_idx, end_idx)]
    # new_list prints every # in range_list from the range of start_idx to end_idx (non inclusive)
    return new_list
    # return new_list. we made new_list so range_list is not mutated


def add_at_index(add_list, add_num, add_idx):
    if add_idx < 0:  # if idx is less than 0, throw an error
        raise IndexError("Index is out of bounds for the input list")
    if add_idx > len(add_list):  # if idx is greater than length of list, throw an error
        raise IndexError("Index is out of bounds for the input list")
    add_list.append(None)  # first, add empty space to end of list
    for elem in range(len(add_list) - 1, add_idx, -1):
        # len(add_list) - 1 represents the last idx of add_list
        # add_idx represents the given idx
        # -1 tells us that the loop will start from end of list and move backwards
        # so, this line tells us that the loop will go over each # from the last idx of add_list to add_idx, moving backwards
        # as loop iterates it will move each elem 1 space to the right
        add_list[elem] = add_list[elem - 1]
        # creates empty space at the idx we want instead of end of list
    add_list[add_idx] = add_num
    # inserts add_num into the empty space
