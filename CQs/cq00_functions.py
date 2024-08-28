"""Functions CQ"""

__author__ = "730652750"


# function def
def mimic(message: str) -> str:
    """Mimic message."""
    return message


# function def
def main() -> None:
    "Main function."
    print(mimic(message=input("What is your message?")))


# called conditional statement; indented code beneath if statement will be run in the "Run" tab in trailhead, doesnt work in "Interact" tab
if __name__ == "__main__":
    main()
