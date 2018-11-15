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