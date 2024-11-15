"""11/15/24 - Linked List Utility Functions Exercise."""

from __future__ import annotations

__author__ = "730745467"


class Node:
    """Creates the Node Class."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None) -> None:
        """Creates a new instance of Node."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Represent an object as a str."""
        rest: str = "?"
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


three: Node = Node(3, None)
two: Node = Node(2, three)
one: Node = Node(1, two)

courses: Node = Node(110, Node(210, Node(301, None)))


def to_str(head: Node | None) -> str:
    """Represent a linked list as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


def last(head: Node) -> int:
    """Return the last value in a linked list."""
    if head.next is None:
        return head.value
    else:
        return last(head.next)


def recursive_range(start: int, end: int) -> Node | None:
    """Build a linked list recursively from start up until end (non-inclusive)."""
    if start > end:
        raise Exception("Invalid use of recursive_range")

    if start == end:
        return None
    else:
        return Node(start, recursive_range(start + 1, end))


def value_at(head: Node | None, index: int) -> int:
    """Return the value of a Node at an index of the linked list."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")

    if index == 0:
        return head.value
    else:
        return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Returns the value of the highest value Node."""
    if head is None:
        raise ValueError("Cannot call max with None")

    if head.next is None:
        return head.value
    else:
        current: int = head.value
        next_highest: int = max(head.next)
        if current < next_highest:
            current = next_highest

    return current


def linkify(items: list[int]) -> Node | None:
    """Creates a linked list of Nodes when given a list of values."""
    if items == []:
        return None
    else:
        new_list: list[int] = items[1:]
        return Node(items[0], linkify(new_list))


def scale(head: Node | None, factor: int) -> Node | None:
    """Increase the value of all Nodes in a linked list by a factor."""
    if head is None:
        return None
    else:
        return Node(head.value * factor, scale(head.next, factor))
