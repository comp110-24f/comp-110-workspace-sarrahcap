"""Plan the best tea party ever."""

__author__: str = "730652750"


# for cost, you cannot do any arithmetic in the print function, you must call on the other function definitions (while still defining the necessary parameters)
def main_planner(guests: int) -> None:
    """Calculates number of tea bags and treats needed along with cost based on number of guests."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Compute number of tea bags needed based on number of guests"""
    return people * 2


# make sure to define what the parameter people means (in this case, people=people because people refers to the number of people in the tea_bags function)
def treats(people: int) -> int:
    """Compute number of treats needed based on amount of tea that has been consumed."""
    return people + tea_bags(people=people)


# tea_count refers to number of tea bags, treat_count refers to number of treats. both numbers are multiplied by their cost and then added together for the total cost of both treats and tea bags
def cost(tea_count: int, treat_count: int) -> float:
    """Cost of tea bags and treats."""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
