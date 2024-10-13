"""List Utility Functions"""

__author__ = "730652750"


def all(list_1: list[int], int_1):
    if not list_1:
        return False
    # if list is empty, return False
    for elem in list_1:
        if elem != int_1:
            return False
        # if int_1 is not in list, return False. use for ... in loop to iterate over every value in list
    return True
    # if int_1 is in list, return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max () arg is an empty List")
    max_value = input[0]
    # set max_value equal to first # in list
    for elem in input:
        if elem > max_value:
            max_value = elem
            # use for ... in loop to iterate over every value in list. if # in list is greater than 1st # in list, that # becomes the max_value. similar to card analogy from class
    return max_value
    # after comparing max_value to #'s in list, return the found max_value


def is_equal(int_list_1: list[int], int_list_2: list[int]):
    # if return type is a bool, do not write it in function signature or it will give an error
    if int_list_1 == int_list_2:
        return True
    # if the two lists are equal, return true
    if int_list_1 != int_list_2:
        return False
    # if the two lists are not equal, return false


def extend(i_list_1: list[int], i_list_2: list[int]):
    for elem in i_list_2:
        # use for ... in loop so it will iterate over every value of i_list_2
        i_list_1.append(elem)
        # add all elems of i_list_2 to end of i_list_1
        # do not need to write return __ at the end because it is not returning anything, just mutating
        # if you write return i_list_1 it will only return original list, not the appended list
