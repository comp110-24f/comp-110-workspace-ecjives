"""10/16/24 - Max Test Challenge Question"""

__author__ = "730745467"


def find_and_remove_max(whole_list: list[int]) -> int:

    if whole_list == []:

        return -1
    else:
        maximum: int = whole_list[0]
        for number in whole_list:

            if number > maximum:

                maximum = number

        index: int = 0
        while index < len(whole_list):

            if whole_list[index] == maximum:

                whole_list.pop(index)
                index -= 1
            index += 1
        return maximum


test: list[int] = [1, 2, 3, 4, 4, 2]
print(find_and_remove_max(test))
print(test)
