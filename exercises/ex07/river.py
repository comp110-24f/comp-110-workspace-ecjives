"""File to define River class."""

__author__ = "730745467"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Class definition of River."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """Initialize a new instance of River."""
        self.day: int = 0
        self.fish: list[Fish] = []
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        self.bears: list[Bear] = []
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes any Fish or Bears over a certain age."""
        new_fish: list[Fish] = []
        for fishy in self.fish:
            if fishy.age <= 3:
                new_fish.append(fishy)
        self.fish = new_fish

        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(bear)
        self.bears = new_bears

    def bears_eating(self):
        """Simulates Bear eating if there's enough Fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self):
        """Removes a Bear if it's hunger is too low."""
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_bears.append(bear)
        self.bears = new_bears

    def remove_fish(self, amount: int):
        """Removes a specified number of Fish."""
        for _ in range(0, amount):
            self.fish.pop(0)

    def repopulate_fish(self):
        """For each pair of Fish, 4 more Fish are added."""
        for _ in range(0, ((len(self.fish) // 2) * 4)):
            self.fish.append(Fish())

    def repopulate_bears(self):
        """For each pair of Bear, 1 more Bear is added."""
        for _ in range(0, (len(self.bears) // 2)):
            self.bears.append(Bear())

    def view_river(self):
        """Shows the current stats of River."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulates one day in River."""
        # Increase day by 1
        self.day += 1

        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()

        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()

        # Simulate Bear's eating
        self.bears_eating()

        # Remove hungry Bear's from River
        self.check_hunger()

        # Remove old Fish and Bear's from River
        self.check_ages()

        # Simulate Fish repopulation
        self.repopulate_fish()

        # Simulate Bear repopulation
        self.repopulate_bears()

        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Runs the simulation over seven days."""
        for _ in range(0, 7):
            self.one_river_day()
