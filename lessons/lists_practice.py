"""Basic syntax of lists."""

# empty list; [] is literal, list() is constructor
my_numbers: list[float] = []
my_numbers: list[float] = list()

# print(my_numbers)

# my_name: str = "" (#empty string literal)
# my_name: str = str() (#empty string constructor)

# appending a list
# my_numbers.append(1.5)
# my_numbers.append(2.3)
# print(my_numbers)

## creating an already populated list
game_points: list[int] = [102, 86, 94]
# print(game_points)
game_points[1] = 72  # changing list value by indexing
# print(game_points)
game_points.pop(1)  # removing values
# print(game_points)
# print(game_points[2])  # indexing
# last_game: int = game_points[2]  # storing as a variable
# print(last_game)
# print(len(game_points)) #tells length


# class_num: str = "110"  # change it to "210"
# class_num[0] = "2" #doesnn't work for strings


# function name: display
# parameter: list of integers
# RV: none
# print every element in the input list
# call display on game_points


def display(int_list: list[int]) -> None:
    """Displays all elements of int_list"""

    index: int = 0

    while index < len(int_list):
        print(int_list[index])
        index += 1


display(int_list=game_points)
