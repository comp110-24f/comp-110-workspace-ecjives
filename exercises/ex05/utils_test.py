"""10/14/24 - List Utils Exercise"""

__author__ = "730745467"

from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens_empty() -> None:

    test_list: list[int] = []
    assert only_evens(test_list) == []


def test_only_evens_return() -> None:

    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    assert only_evens(test_list) == [2, 4, 6, 8]


def test_only_evens_mutation() -> None:

    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    only_evens(test_list)
    assert test_list == [1, 2, 3, 4, 5, 6, 7, 8]


def test_sub_range() -> None:

    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    assert sub(test_list, -5, 20) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_sub_return() -> None:

    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    assert sub(test_list, 2, 6) == [3, 4, 5, 6]


def test_sub_mutation() -> None:

    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    sub(test_list, 2, 4)
    assert test_list == [1, 2, 3, 4, 5, 6, 7, 8]


def test_add_at_index_empty() -> None:

    test_list: list[int] = []
    add_at_index(test_list, 2, 0)
    assert test_list == [2]


def test_add_at_index_return() -> None:

    test_list: list[int] = [1, 2, 4]
    assert add_at_index(test_list, 3, 2) is None


def test_add_at_index_mutation() -> None:

    test_list: list[int] = [1, 2, 4]
    add_at_index(test_list, 3, 2)
    assert test_list != [1, 2, 4]
