import ships

class Player():
    def __init__(self, enemy):
        self.enemy = enemy

    def setup(self, arr_of_ships, board):
        for ship in arr_of_ships:
            new_ship = ships.Ships(ship[0], size)