"""10/14/24 - List Utils Exercise"""

__author__ = "730745467"


def only_evens(whole_list: list[int]) -> list[int]:

    even_list: list[int] = []
    for number in whole_list:

        if number % 2 == 0:

            even_list.append(number)
    return even_list


def sub(whole_list: list[int], start: int, end: int) -> list[int]:

    new_list: list[int] = []
    for index in range(start, end):

        if (index >= 0) and (index < len(whole_list)):

            new_list.append(whole_list[index])
    return new_list


def add_at_index(whole_list: list[int], number: int, index: int) -> None:

    if (index < 0) or (index > len(whole_list)):

        raise IndexError("Index is out of bounds for the input list")
    elif index == len(whole_list):
        whole_list.append(number)
    else:

        whole_list.insert(index, number)


list_1: list[int] = [2]

# print(only_evens(list_1))
# print(sub(list_1, -1, 5))
print(list_1)
add_at_index(list_1, 4, 1)
print(list_1)
