"""Defining unit tests for utils."""

__author__ = "730652750"


from exercises.ex05.utils import only_evens, sub, add_at_index, pytest


def test_only_evens() -> None:
    """Testing only_evens function returns new list of only even values."""
    combined_list: list[int] = [4, 5, 6, 7]
    assert only_evens(combined_list) == [4, 6]
    combined_list_2: list[int] = [6, 7, 4, 6, 9]
    assert only_evens(combined_list_2) == [6, 4, 6]
    """Testing only_evens function returns empty list for empty input."""
    empty_list: list[int] = []
    assert only_evens(empty_list) == []


def test_sub() -> None:
    """Testing sub function generates a new list between the start index and end index -1."""
    correct_list: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(correct_list, 1, 5) == [2, 3, 4, 5]
    correct_list_2: list[int] = [2, 5, 10, 100, 500]
    assert sub(correct_list_2, 1, 4) == [5, 10, 100]
    """Testing sub function returns empty list when empty list is inputted."""
    wrong_list: list[int] = []
    assert sub(wrong_list, 1, 4) == []


def test_add_at_index() -> None:
    """Testing add_at_index function modifies inputted list to place element at given index."""
    add_list: list[int] = [2, 4, 6, 10]
    assert add_at_index(add_list, 8, 3) == [2, 4, 6, 8, 10]
    add_list_2: list[int] = [5, 10, 15]
    assert add_at_index(add_list_2, 20, 3) == [5, 10, 15, 20]


def test_add_at_index_raises_indexerror():
    """Test that add_at_index rasies an IndexError for an invalid index."""
    list_add: list[int] = [1, 2, 3]
    with pytest.raises(IndexError):
        add_at_index(list_add, -1, 4)
