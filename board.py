

class Board:
    def __init__(self, size):
        import main
        self.board = size * [main.EMPTY]
        self.ships = 0

    def fire(self, location):
        import main
        "Takes number input and modifies board"
        if self.board[location] == main.SHIP:
            self.board[location] = main.HIT
            self.ships -= 1
            return True
        elif self.board[location] in (main.MISS, main.HIT):
            return False
        else:
            self.board[location] = main.MISS
            return False

    def add_ship(self, location):
        import main
        for pos in location:
            self.board[pos] = main.SHIP

    def render(self):
        import main
        output = "  | "
        output += " | ".join(i for i in main.TOP)
        for row in range(10):
            output += "\n" + (41 * "-") + "\n" + main.SIDE[row] + " "
            for col in range(10):
                output += "| %s " % self.board[row * 10 + col]
        output += "\n" + (41 * "-")
        return output

    def legal_ship(self, location):
        "Checks [0, 1] coordinates for map and ship intersection"
        import main

        direction = location[1] - location[0]

        for pos in location:
            if not (0 <= pos <= 99) or self.board[pos] == main.SHIP:
                return False

        if abs(direction) == 1 and int(location[0] / 10) != int(location[-1] / 10):
            return False

        return True