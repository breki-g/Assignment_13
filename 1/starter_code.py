from typing import Tuple


# Constants
NORTH = "n"
EAST = "e"
SOUTH = "s"
WEST = "w"

STARTING_LOCATION = (1, 1)
FINAL_DESTINATION = (3, 1)


coins = 0
lever = False

def main():
    location = STARTING_LOCATION
    while location != FINAL_DESTINATION:
        location = play_one_move(location)
        if location == FINAL_DESTINATION:
            print("Victory! Total coins", coins, end=".\n")
            if play_again():
                location = STARTING_LOCATION
    #print("Victory! Total coins", coins, end=".")
    


def play_one_move(location: Tuple[int]) -> Tuple[int]:
    """Plays one move of the game.

    Returns updated location.
    """

    valid_directions = find_directions(location)
    direction = get_direction(valid_directions)

    if direction in valid_directions:
        location = move(direction, location)
        #added
        check_lever(location)
    else:
        print("Not a valid direction!")

    #coins, lever = check_lever(coins)      #Test

    return location


def find_directions(location: Tuple[int]) -> Tuple[str]:
    """Returns valid directions as a string given the supplied location."""
    
    if location == (1, 1):

        valid_directions = (NORTH,)
    elif location == (1, 2):
        

        valid_directions = NORTH, EAST, SOUTH
    elif location == (1, 3):

        valid_directions = EAST, SOUTH
    elif location == (2, 1):

        valid_directions = (NORTH,)
    elif location == (2, 2):
        

        valid_directions = SOUTH, WEST
    elif location == (2, 3):
        

        valid_directions = EAST, WEST
    elif location == (3, 2):
        

        valid_directions = NORTH, SOUTH
    elif location == (3, 3):
 
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

def check_lever(location: Tuple[int]) -> None:
    
    global coins, lever
    lever_rooms = [(1, 2), (2, 2), (2, 3), (3, 2)]
    if location in lever_rooms:
        lever_input = input("Pull a lever (y/n):")
        print("")
        lever_answer = lever_input.lower()
        if lever_answer == "y":
            coins += 1
            
            print("You received 1 coin, your total is now ", coins, end=".\n")

            #lever = False
    #return lever
def play_again():
    global coins
    reset_input = input("Play again (y/n):" )
    reset_answer = reset_input.lower()
    if reset_answer == "y":
        coins = 0
        again = True
        print("")
        
    else:
        again = False

    return again


if __name__ == "__main__":
    main()
