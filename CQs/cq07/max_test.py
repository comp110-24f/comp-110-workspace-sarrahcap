"""Unit Test"""

__author__ = "730652750"


from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_returns_expected(list: list[int]) -> None:
    assert find_and_remove_max([4, 5, 6, 7]) == 7


def test_find_and_remove_max_mutates(list: list[int]) -> None:
    assert find_and_remove_max([4, 5, 6, 7]) == [4, 5, 6]


def test_find_and_remove_max_unconventional(list: list[int]) -> None:
    assert find_and_remove_max([]) == -1
