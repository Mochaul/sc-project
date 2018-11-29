
class AI:
    def __init__(self, difficulty, enemy):
        self.difficulty = difficulty
        self.mode = "HUNT"
        self.enemy = enemy
        self.modelist = {"HUNT": self.hunt, "ACQUIRE": self.acquire, "DESTROY": self.destroy}

    def setup(self, board):
        from random import choice, randint
        import main
        for ship in main.ships:
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
        import main
        result = self.modelist[self.mode]()
        if end:
            if result[0]:
                print("\nComputer hit %s" % main.inv_gridconvert(result[1]))
            else:
                print("\nComputer missed %s" % main.inv_gridconvert(result[1]))

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