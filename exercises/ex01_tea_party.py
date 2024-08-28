"""8/26/24 - Tea Party Exercise"""

__author__ = "730745467"

def main_planner(guests: int) -> None:
    """Plans a tea party using the number of guests"""
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats " + str(treats(guests)))
    print("Cost: " + str(cost(tea_bags(guests), treats(guests))))

def tea_bags(people: int) -> int:
    """Calculates the number of tea bags needed"""
    return people * 2
def treats(people: int) -> int:
    """Calculates the number of treats needed"""
    return people * 3
def cost(tea_bag_count: int, treat_count: int) -> float:

    """Calculates the total cost"""
    return (tea_bag_count * 0.5) + (treat_count * 0.75)

if __name__ == "__main__":
    main_planner(int(input("How many guests are attending the tea party? ")))