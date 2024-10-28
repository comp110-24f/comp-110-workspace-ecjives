"""10/27/24 - Dictionaries Exercise"""

__author__ = "730745467"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values in a dictionary"""

    new_dictionary: dict[str, str] = {}
    for x in dictionary:
        if dictionary[x] in new_dictionary:
            raise KeyError("error message of your choice here!")
        else:
            new_dictionary[dictionary[x]] = x
    return new_dictionary


def favorite_color(colors: dict[str, str]) -> str:
    """Looks through a dictionary of people's favorite colors and returns the most frequent"""

    score_dictionary: dict[str, int] = {"None": 0}
    highest: str = "None"
    if colors == {}:
        return ""

    for person in colors:

        if colors[person] in score_dictionary:
            score_dictionary[colors[person]] += 1
        else:
            score_dictionary[colors[person]] = 1

    for color in score_dictionary:
        if score_dictionary[color] > score_dictionary[highest]:
            highest = color
    score_dictionary.pop("None")
    return highest


def count(full_list: list[str]) -> dict[str, int]:
    """Counts the number of times a string appears in a list"""

    count_dictionary: dict[str, int] = {}
    for item in full_list:

        if item in count_dictionary:
            count_dictionary[item] += 1
        else:
            count_dictionary[item] = 1
    return count_dictionary


def alphabetizer(full_list: list[str]) -> dict[str, list[str]]:
    """Organizes strings into a list based on their first letter"""

    alphabet_dictionary: dict[str, list[str]] = {}
    for word in full_list:
        if word.lower()[0] not in alphabet_dictionary:
            alphabet_dictionary[word.lower()[0]] = []
        alphabet_dictionary[word.lower()[0]].append(word)
    return alphabet_dictionary


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Adds names of students to a list under a corresponding day"""

    if day not in attendance:
        attendance[day] = []

    if student not in attendance[day]:
        attendance[day].append(student)
    return None


"""test_dictionary: dict[str, str] = {
    "chocolate": "one",
    "vanilla": "eight",
    "strawberry": "four",
}
print(test_dictionary)
print(invert(test_dictionary))

test_dictionary_1: dict[str, str] = {
    "alpha": "green",
    "beta": "blue",
    "charlie": "green",
    "delta": "green",
    "echo": "red",
    "foxtrot": "red",
    "golf": "purple",
    "hotel": "blue",
    "indigo": "red",
}
print(favorite_color(test_dictionary_1))

test_list: list[str] = ["one", "two", "two", "three", "three", "three"]
print(count(test_list))

if "a" < "b":
    print("True")

word: str = "Word"
print(word.lower()[0])"""
