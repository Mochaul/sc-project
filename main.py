from board import *
from player import *
from ai import *
from gui import *

def main():
    app = gui.GUI()

    global SHIP, HIT, MISS, EMPTY
    global TOP, SIDE
    global ships
    
    SHIP = "S"
    HIT = "X"
    MISS = "O"
    EMPTY = " "

    TOP = "ABCDEFGHIJ"
    SIDE = "0123456789"

    #ships = [["Carriers", 5, 1]] #Use while testing
    ships = [["Carrier", 5, 1], ["Battleships", 4, 2], ["Cruisers", 3, 2], ["Submarines", 2, 1]]

    functions()

    def fullgame():
        global user_board, comp_board
        global user, comp
        
        user_board = Board(100)
        comp_board = Board(100)

        user = Player(comp_board)
        comp = AI(1, user_board)

        user.setup(user_board)
        comp.setup(comp_board)

        while (user_board.ships and comp_board.ships) > 0:
            user.turn()
            if comp_board.ships > 0:
                comp.turn()
                print("Here is your board:")
                print(user_board.render())
                
        if user_board.ships > 0:
            winner = ["You", user_board.ships]
        else:
            winner = ["The computer", comp_board.ships]
        print("\nGame over.\n%s won with %s ships remaining" % (winner[0], winner[1]))

    def ai_test():
        user_board = Board(100)
        user_board.ships = 101
        comp = AI(0, user_board)

        while True:
            comp.turn()
            print(user_board.render())
            input()

    fullgame()

    app.mainloop()

def functions():
    global gridconvert, inv_gridconvert, gen_poslist, onboard, \
           check_diagonal, grid_picktile, getdirs, getdirs_ext
    
    def gridconvert(location):
        "Turns A0 coordinates into grid numbers"
        location = TOP.find(location[0]) + (SIDE.find(location[1]) * 10)
        return location

    def inv_gridconvert(location):
        "Turns grid numbers into A0 coordinates"
        location = TOP[location % 10] + SIDE[int(location / 10)]
        return location

    def gen_poslist(location, length):
        "Turns [1, 2] coordinates and length into list of grid numbers"
        direction = location[1] - location[0]
        if abs(direction) >= 10:
            if direction < 0:
                direction = -10
            else:
                direction = 10
        else:
            if direction < 0:
                direction = -1
            else:
                direction = 1
        location = [location[0], location[0] + direction]

        poslist = []
        for pos in range(location[0], location[0] + (length * direction), direction):
            poslist += [pos]
            
        return poslist

    def onboard(coords):
        "Checks if A0 coordinates are on the board"
        if coords[0] in TOP and coords[1] in SIDE:
            return True
        else:
            return False

    def check_diagonal(location):
        "Returns True if [0, 1] coordinates are diagonal"
        if location[0] % 10 == location[1] % 10 or \
           int(location[0] / 10) == int(location[1] / 10):
            return False
        else:
            return True

    def grid_picktile():
        "Chooses a tile from grid"
        from random import randrange
        target = randrange(0, 91, 10)
        target += randrange((target // 10) % 2, 10, 2)
        return target

    def getdirs(pos):
        "Returns avaliable directions from pos"
        output = []
        if pos % 10 != 9: output += [1]
        if pos % 10 != 0: output += [-1]
        if pos < 90: output += [10]
        if pos > 9: output += [-10]
        return output

    def getdirs_ext(pos):
        "Returns extended available directions from pos"
        from itertools import combinations
        output = getdirs(pos)
        for comb in combinations(output, 2):
            if sum(comb) != 0:
                output += [sum(comb)]
        return output

main()