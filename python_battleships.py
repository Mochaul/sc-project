#Battleships 5

def main():
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
        comp = AI(100, user_board) #Difficulty up to 10

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

################################

################################

class Board:
    def __init__(self, size):
        self.board = size * [EMPTY]
        self.ships = 0

    def fire(self, location):
        "Takes number input and modifies board"
        if self.board[location] == SHIP:
            self.board[location] = HIT
            self.ships -= 1
            return True
        elif self.board[location] in (MISS, HIT):
            return False
        else:
            self.board[location] = MISS
            return False

    def add_ship(self, location):
        for pos in location:
            self.board[pos] = SHIP

    def render(self):
        output = "  | "
        output += " | ".join(i for i in TOP)
        for row in range(10):
            output += "\n" + (41 * "-") + "\n" + SIDE[row] + " "
            for col in range(10):
                output += "| %s " % self.board[row * 10 + col]
        output += "\n" + (41 * "-")
        return output

    def legal_ship(self, location):
        "Checks [0, 1] coordinates for map and ship intersection"

        direction = location[1] - location[0]

        for pos in location:
            if not (0 <= pos <= 99) or self.board[pos] == SHIP:
                return False

        if abs(direction) == 1 and int(location[0] / 10) != int(location[-1] / 10):
            return False

        return True

class Player():
    def __init__(self, enemy):
        self.enemy = enemy
    
    def setup(self, board):
        print(user_board.render())
        print("Enter ship coordinates as \"A0 to A3\"")
        for ship in ships:
            name, length, number = ship[0], ship[1], ship[2]
            print("You have %s %s-long %s" % (number, length, name))
            for i in range(number):
                allocated = False
                while not allocated:
                    location = input("Enter coords: ").upper().split(" ")
                    try: location = [location[0], location[-1]]
                    except:
                        print("Invalid coordinates")
                        continue
                    
                    if not (onboard(location[0]) and onboard(location[1])):
                        print("Coordinates not on board")
                        continue
                    
                    location = [gridconvert(location[0]), gridconvert(location[1])]
                    if check_diagonal(location):
                        print("Diagonal ships are not allowed")
                        continue
                    
                    location = gen_poslist(location, length)
                    if not board.legal_ship(location):
                        print("Ship intersects map or other ships")
                        continue

                    board.add_ship(location)
                    board.ships += length
                    allocated = True

    def turn(self): #Fix redundant firing
        print("Here is the enemy's board:")
        print(self.enemy.render().replace(SHIP, EMPTY))
        valid = False
        while not valid:
            target = input("Enter position to fire at: ").upper()
            try: target = gridconvert(target)
            except:
                print("Invalid coordinates")
                continue
            if self.enemy.board[target] in (MISS, HIT):
                print("You have already fired at that tile")
                continue
            valid = True

        if self.enemy.board[target] == SHIP:
            print("You hit %s" % target)
        else:
            print("You missed %s" % target)
        self.enemy.fire(target)

################################

################################

class AI:
    def __init__(self, difficulty, enemy):
        self.difficulty = difficulty
        self.mode = "HUNT"
        self.enemy = enemy
        self.modelist = {"HUNT": self.hunt, "ACQUIRE": self.acquire, "DESTROY": self.destroy}

    def setup(self, board):
        from random import choice, randint
        for ship in ships:
            length, number = ship[1], ship[2]
            for i in range(number):
                allocated = False
                while not allocated:
                    location = [randint(0, 99), 0]
                    direction = choice(getdirs(location[0]))
                    location[1] = location[0] + direction

                    location = gen_poslist(location, length)

                    if not board.legal_ship(location):
                        continue

                    board.add_ship(location)
                    board.ships += length
                    allocated = True

    def turn(self, end = True):
        result = self.modelist[self.mode]()
        if end:
            if result[0]:
                print("\nComputer hit %s" % inv_gridconvert(result[1]))
            else:
                print("\nComputer missed %s" % inv_gridconvert(result[1]))

    def hunt(self):
        target = self.picktile()

        for i in range(self.difficulty):
            if self.enemy.board[target] == SHIP:
                break
            else:
                target = self.picktile()

        if self.enemy.board[target] == SHIP:
            self.mode = "ACQUIRE"
            self.acqlist = [target]

            for direction in getdirs(target):
                if self.enemy.board[target + direction] not in (MISS, HIT):
                    self.acqlist += [direction]

        return self.enemy.fire(target), target

    def acquire(self):
        target = self.acqlist[0] + self.acqlist[1]

        for i in range(self.difficulty):
            if self.enemy.board[target] == SHIP:
                break
            else:
                self.acqlist.pop(1)
                target = self.acqlist[0] + self.acqlist[1]

        if self.enemy.board[target] == SHIP:
            result = self.enemy.fire(target)
            self.destlist = self.findship(self.acqlist[0], self.acqlist[1])
            self.mode = "DESTROY"
        else:
            result = self.enemy.fire(target)
            self.acqlist.pop(1)

        return result, target

    def destroy(self):
        if len(self.destlist) > 0:
            target = self.destlist[0]
            self.destlist.pop(0)
        else:
            self.mode = "HUNT"
            return self.hunt()
        
        return self.enemy.fire(target), target

    def findship(self, pos, direction):
        poslist = []

        for i in range(2):
            ignore, progpos = False, pos
            while not ignore:
                if check_diagonal([progpos, progpos + direction]) or \
                   progpos + direction < 0:
                    ignore = True
                    continue
                
                progpos += direction
                if self.enemy.board[progpos] == HIT:
                    pass
                elif self.enemy.board[progpos] == EMPTY:
                    poslist += [progpos]
                    ignore = True
                elif self.enemy.board[progpos] == MISS:
                    ignore = True
                else:
                    poslist += [progpos]
            direction *= -1
        return poslist

    def picktile(self):
        target = grid_picktile()
        while self.enemy.board[target] in (MISS, HIT):
            target = grid_picktile()
        return target

main()