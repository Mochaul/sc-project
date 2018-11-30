import board, ai

class Player():
    def __init__(self, enemy):
        self.enemy = enemy
    
    def setup(self, board):
        import main
        print(main.user_board.render())
        print("Masukan koordinat kapal, contoh \"A0 sampai A3\"")
        for ship in main.ships:
            name, length, number = ship[0], ship[1], ship[2]
            print("Kamu punya %s kapal yang panjangnya %s-long yang bernama kapal %s" % (number, length, name))
            for i in range(number):
                allocated = False
                while not allocated:
                    location = input("Masukan koordinat: ").upper().split(" ")
                    try: location = [location[0], location[-1]]
                    except:
                        print("Koordinat salah")
                        continue
                    
                    if not (main.onboard(location[0]) and main.onboard(location[1])):
                        print("Koordinat tidak ada di board")
                        continue
                    
                    location = [main.gridconvert(location[0]), main.gridconvert(location[1])]
                    if main.check_diagonal(location):
                        print("Kapal tidak boleh ditempatkan secara diagonal")
                        continue
                    
                    location = main.gen_poslist(location, length)
                    if not board.legal_ship(location):
                        print("Ada kapal lain di koordinat tersebut")
                        continue

                    board.add_ship(location)
                    board.ships += length
                    allocated = True

    def turn(self): #Fix redundant firing
        import main
        print("Ini laut nelayan nakal yang masuk ke laut Indonesia:")
        print(self.enemy.render().replace(main.SHIP, main.EMPTY))
        valid = False
        while not valid:
            target = input("Masukan koordinat tembak: ").upper()
            try: target = main.gridconvert(target)
            except:
                print("Koordinat tidak sesuai")
                continue
            if self.enemy.board[target] in (main.MISS, main.HIT):
                print("Koordinat tersebut sudah pernah ditembak")
                continue
            valid = True

        if self.enemy.board[target] == main.SHIP:
            print("Terkena pada koordinat %s" % target)
        else:
            print("Meleset pada koordinat %s" % target)
        self.enemy.fire(target)