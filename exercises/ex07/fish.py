"""File to define Fish class."""

__author__ = "730745467"


class Fish:
    """Class definition of Fish."""

    age: int

    def __init__(self):
        """Initialize a new instance of Fish."""
        self.age = 0

    def one_day(self):
        """Updates attribues of Fish after one day."""
        self.age += 1
