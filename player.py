import gui, board, ai

class Player():
    def __init__(self, enemy):
        self.enemy = enemy
    
    def setup(self, board):
        import main
        print(main.user_board.render())
        print("Enter ship coordinates as \"A0 to A3\"")
        for ship in main.ships:
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
                    
                    if not (main.onboard(location[0]) and main.onboard(location[1])):
                        print("Coordinates not on board")
                        continue
                    
                    location = [main.gridconvert(location[0]), main.gridconvert(location[1])]
                    if main.check_diagonal(location):
                        print("Diagonal ships are not allowed")
                        continue
                    
                    location = main.gen_poslist(location, length)
                    if not board.legal_ship(location):
                        print("Ship intersects map or other ships")
                        continue

                    board.add_ship(location)
                    board.ships += length
                    allocated = True

    def turn(self): #Fix redundant firing
        import main
        print("Here is the enemy's board:")
        print(self.enemy.render().replace(SHIP, EMPTY))
        valid = False
        while not valid:
            target = input("Enter position to fire at: ").upper()
            try: target = main.gridconvert(target)
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