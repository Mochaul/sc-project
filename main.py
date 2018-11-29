import tkinter as tk                # python3
from tkinter import font  as tkfont # python3

TOP = "ABCDEFGHIJ"
SIDE = "0123456789"
arr_of_ships = []

class GUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.geometry("1000x800")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label_0 = tk.Label(self, text="WELCOME TO TENGGELAMKAN!", font=("bold", 15))
        label_11 = tk.Label(self, text="Format penulisan 'X sampai X' (misal A4 sampai A9)", font=("bold", 10))
        label_0.place(x=70, y=53)
        label_11.place(x=90, y=100)
        self.board = 100 * [" "]
        label_1 = tk.Label(self, text="Kapal Martadinata (5)", width=20, font=("bold", 10))
        label_1.place(x=80, y=130)
        label_2 = tk.Label(self, text="Kapal Fatahillah (4)", width=20, font=("bold", 10))
        label_2.place(x=68, y=180)
        label_3 = tk.Label(self, text="Kapal Cakra (3)", width=20, font=("bold", 10))
        label_3.place(x=70, y=230)
        label_4 = tk.Label(self, text="Kapal Boa (3)", width=20, font=("bold", 10))
        label_4.place(x=70, y=280)
        label_5 = tk.Label(self, text="Kapal Andau (2)", width=20, font=("bold", 10))
        label_5.place(x=85, y=330)
        label_6 = tk.Label(self, text=self.render())
        label_6.place(x = 80, y = 430)

        self.var = tk.StringVar(self) 
        option_menu = tk.OptionMenu(self, self.var, "easy","medium","hard") 
        option_menu.place(x=200,y=350)

        self.entry_1 = tk.Entry(self)
        self.entry_1.place(x=240, y=130)
        self.entry_2 = tk.Entry(self)
        self.entry_2.place(x=240, y=180)
        self.entry_3 = tk.Entry(self)
        self.entry_3.place(x=240, y=230)
        self.entry_4 = tk.Entry(self)
        self.entry_4.place(x=240, y=280)
        self.entry_5 = tk.Entry(self)
        self.entry_5.place(x=240, y=330)
        self.button = tk.Button(self, text="check", command=self.on_button)
        self.button_2 = tk.Button(self, text="next", command= lambda : controller.show_frame("PageOne"))
        self.button.place(x=130, y = 380)
        self.button_2.place(x= 240, y = 380)

    def on_button(self):
        pos_1 = self.entry_1.get()
        pos_2 = self.entry_2.get()
        pos_3 = self.entry_3.get()
        pos_4 = self.entry_4.get()
        pos_5 = self.entry_5.get()
        option = self.var.get()
        self.entry_1.delete(0, 'end')
        self.entry_2.delete(0, 'end')
        self.entry_3.delete(0, 'end')
        self.entry_4.delete(0, 'end')
        self.entry_5.delete(0, 'end')
        if (pos_1[0] in TOP and pos_2[0] in TOP and pos_3[0] in TOP and pos_4[0] in TOP and pos_5[0] in TOP
                and pos_1[-2] in TOP and pos_2[-2] in TOP and pos_3[-2] in TOP and pos_4[-2] in TOP and pos_5[-2] in TOP and
                pos_1[1] in SIDE and pos_2[1] in SIDE and pos_3[1] in SIDE and pos_4[1] in SIDE and pos_5[1] in SIDE
                and pos_1[-1] in SIDE and pos_2[-1] in SIDE and pos_3[-1] in SIDE and pos_4[-1] in SIDE and pos_5[
                    -1] in SIDE):
            arr_ship_1 = ["Kapal Martadinata", 5, 1, pos_1]
            arr_ship_2 = ["Kapal Fatahillah", 4, 1, pos_2]
            arr_ship_3 = ["Kapal Cakra", 3, 1, pos_3]
            arr_ship_4 = ["Kapal Boa", 3, 1, pos_4]
            arr_ship_5 = ["Kapal Andau", 2, 1, pos_5]
            arr_of_ships = [arr_ship_1,arr_ship_2,arr_ship_3,arr_ship_4,arr_ship_5, option]
            print(arr_of_ships)

    def render(self):
        output = "      |  "
        output += "  |   ".join(i for i in TOP)
        for row in range(10):
            output += "\n" + (55* "-") + "\n" + SIDE[row] + " "
            for col in range(10):
                output += "    | %s " % self.board[row * 10 + col]
        output += "\n" + (55 * "-")
        return output


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        left = tk.Frame(self, borderwidth=2, relief="solid")
        right = tk.Frame(self, borderwidth=2, relief="solid")
        self.board = 100 * [" "]
        label2 = tk.Label(left, text="Pembela Tanah Air")
        self.text_tembak = tk.StringVar(self)
        button1 = tk.Button(left, text="Tenggelamkan!", command=self.on_button)
        self.entry_8 = tk.Entry(left, textvariable = self.text_tembak)
        label15 = tk.Label(left, text= self.render())
        label3 = tk.Label(right, text="Nelayan Ilegal")
        label14 = tk.Label(right, text=self.render())

        left.pack(side="left", expand=True, fill="both")
        right.pack(side="right", expand=True, fill="both")
        label2.pack()
        self.entry_8.pack()
        button1.pack()
        label15.pack()
        label3.pack()
        label14.pack()

    def render(self):
        output = "      |  "
        output += "  |   ".join(i for i in TOP)
        for row in range(10):
            output += "\n" + (55* "-") + "\n" + SIDE[row] + " "
            for col in range(10):
                output += "    | %s " % self.board[row * 10 + col]
        output += "\n" + (55 * "-")
        return output


    def on_button(self):
        pos = self.entry_8.get()
        if (len(pos)!=2):
            print ("input tidak valid masukan input yang valid")
        else :
            if (pos[0].upper() not in TOP):
                print ("input tidak valid masukan input yang valid")
            else :
                if (pos[1] not in SIDE):
                    print("input tidak valid masukan input yang valid")
                else :
                    return pos
        print(self.entry_8.get())
        self.entry_8.delete(0, 'end')

# if __name__ == "__main__": 
#     app = GUI() 
#     app.mainloop()

def main():
    app = GUI()
    app.mainloop()

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
        comp = AI(0, user_board)

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