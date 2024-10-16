"""9/18/24 - While Loops Challenge Question"""

__author__ = "730745467"


def num_instances(phrase: str, search_char: str) -> None:
    index: int = 0
    count: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1
    print(count)
