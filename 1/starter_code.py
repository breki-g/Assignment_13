from typing import Tuple


# Constants
NORTH = "n"
EAST = "e"
SOUTH = "s"
WEST = "w"

STARTING_LOCATION = (1, 1)
FINAL_DESTINATION = (3, 1)


coins = 0

def main():
    location = STARTING_LOCATION
    while location != FINAL_DESTINATION:
        location = play_one_move(location)

    print("Victory!")


def play_one_move(location: Tuple[int]) -> Tuple[int]:
    """Plays one move of the game.

    Returns updated location.
    """

    valid_directions = find_directions(location)
    direction = get_direction(valid_directions)

    if direction in valid_directions:
        location = move(direction, location)
    else:
        print("Not a valid direction!")

    #coins, lever = islever(coins)      #Test

    return location


def find_directions(location: Tuple[int]) -> Tuple[str]:
    """Returns valid directions as a string given the supplied location."""
    lever = False
    if location == (1, 1):
        islever(lever)
        valid_directions = (NORTH,)
    elif location == (1, 2):
        lever = True
        islever(lever)
        valid_directions = NORTH, EAST, SOUTH
    elif location == (1, 3):
        islever(lever)
        valid_directions = EAST, SOUTH
    elif location == (2, 1):
        islever(lever)
        valid_directions = (NORTH,)
    elif location == (2, 2):
        lever = True
        islever(lever)
        valid_directions = SOUTH, WEST
    elif location == (2, 3):
        lever = True
        islever(lever)
        valid_directions = EAST, WEST
    elif location == (3, 2):
        lever = True
        islever(lever)
        valid_directions = NORTH, SOUTH
    elif location == (3, 3):
        islever(lever)
        valid_directions = SOUTH, WEST

    return valid_directions


def get_direction(valid_directions: Tuple[str]) -> str:
    print_directions(valid_directions)
    return input("Direction:\n").lower()


def print_directions(available_directions: Tuple[str]) -> None:
    print("You can travel: ", end="")

    one_done_already = False
    for direction in available_directions:
        if one_done_already:
            print(" or ", end="")

        if direction == NORTH:
            print("(N)orth", end="")
        elif direction == EAST:
            print("(E)ast", end="")
        elif direction == SOUTH:
            print("(S)outh", end="")
        elif direction == WEST:
            print("(W)est", end="")

        one_done_already = True

    print(".")


def move(direction: str, location: Tuple[int]) -> Tuple[int]:
    """Returns updated location given the direction."""

    x, y = location

    if direction == NORTH:
        y += 1
    elif direction == SOUTH:
        y -= 1
    elif direction == EAST:
        x += 1
    elif direction == WEST:
        x -= 1

    return x, y

def islever(lever: bool):
    
    global coins
    if lever:
        lever_input = input("Pull a lever (y/n):")
        lever_answer = lever_input.lower()
        if lever_answer == "y":
            coins += 1
            print("You received 1 coin, your total is now ", coins, ".")
            lever = False
    return lever



if __name__ == "__main__":
    main()
