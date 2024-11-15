"""File to define Bear class."""

__author__ = "730745467"


class Bear:
    """Class definition of Bear."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initialize a new instance of Bear."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """Updates attributes of Bear after one day."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """Updates hunger_score of Bear after eating."""
        self.hunger_score += num_fish
