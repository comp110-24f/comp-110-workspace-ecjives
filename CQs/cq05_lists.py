"""10/4/24 - Mutating Functions Challenge Question"""

__author__ = "730745467"


def manual_append(list: list[int], new_item: int) -> None:

    list.append(new_item)


def double(list: list[int]) -> None:

    index: int = 0
    while index < len(list):

        list[index] *= 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(list_1)
print(list_2)
