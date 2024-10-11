"""10/4/24 - List Utility Exercise"""

__author__ = "730745467"


def all(list: list[int], number: int) -> bool:

    index: int = 0

    if len(list) == 0:

        return False
    while index < len(list):

        if list[index] != number:

            return False
        index += 1
    return True


def max(list: list[int]) -> int:

    index: int = 0
    largest: int = list[0]

    if len(list) == 0:

        raise ValueError("max() arg is an empty List")
    while index < len(list):
        if list[index] > largest:
            largest = list[index]
        index += 1
    return largest


def is_equal(list_1: list[int], list_2: list[int]) -> bool:

    index: int = 0

    if len(list_1) == 0 and len(list_2) == 0:

        return True
    if len(list_1) != len(list_2):

        return False
    while index < len(list_1):

        if list_1[index] != list_2[index]:

            return False
        index += 1
    return True


def extend(list_1: list[int], list_2: list[int]) -> None:

    index: int = 0

    while index < len(list_2):

        list_1.append(list_2[index])
        index += 1
