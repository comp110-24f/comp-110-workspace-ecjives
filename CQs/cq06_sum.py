"""10/9/24 - List Sum Challenge Question"""

__author__ = "730745467"


def w_sum(list: list[float]) -> float:

    sum: float = 0.0
    if len(list) == 0:
        return sum
    else:
        index: int = 0
        while index < len(list):
            sum += list[index]
            index += 1
        return sum


def f_sum(list: list[float]) -> float:

    sum: float = 0.0
    if len(list) == 0:
        return sum
    else:
        for number in list:
            sum += number
        return sum


def f_range_sum(list: list[float]) -> float:

    sum: float = 0.0
    if len(list) == 0:
        return sum
    else:
        for index in range(0, len(list)):
            sum += list[index]
        return sum
