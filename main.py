def main():
    global SHIP, HIT, MISS, EMPTY
    global TOP, SIDE
    global ships
    
    # Set the ship for the terminal interface
    SHIP = "S"
    HIT = "X"
    MISS = "O"
    EMPTY = " "

    TOP = "ABCDEFGHIJ"
    SIDE = "0123456789"

    # Available ships for the game
    ships = [["Carrier", 5, 1], ["Battleships", 4, 2], ["Cruisers", 3, 2], ["Submarines", 2, 1]]