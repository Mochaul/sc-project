import gui

def main():
    app = gui.GUI()
    # Available ships for the game
    # ships = [["Carrier", 5, 1], ["Battleships", 4, 2], ["Cruisers", 3, 2], ["Submarines", 2, 1]]

    #functions()

    def fullgame():
        global user_board, comp_board
        global user, comp
        
        # Set the board
        user_board = Board(100)
        comp_board = Board(100)

    app.mainloop()

main()