class Board:
    def __init__(self, size):
        self.board = size * [EMPTY]
        self.ships = 0


    def add_ship(self, location):
        for pos in location:
            self.board[pos] = SHIP

    def cetak(self):
        output = "  | "
        output += " | ".join(i for i in TOP)
        for row in range(10):
            output += "\n" + (41 * "-") + "\n" + SIDE[row] + " "
            for col in range(10):
                output += "| %s " % self.board[row * 10 + col]
        output += "\n" + (41 * "-")
        return output
