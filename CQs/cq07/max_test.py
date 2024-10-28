"""10/16/24 - Max Test Challenge Question"""

__author__ = "730745467"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_empty() -> None:

    test_list: list[int] = []
    assert find_and_remove_max(test_list) == -1


def test_find_and_remove_max_return() -> None:

    test_list: list[int] = [1, 4, 4, 3, 2]
    assert find_and_remove_max(test_list) == 4


def test_find_and_remove_max_mutate() -> None:

    test_list: list[int] = [1, 4, 4, 3, 2]
    find_and_remove_max(test_list)
    assert test_list != [1, 4, 4, 3, 2]
