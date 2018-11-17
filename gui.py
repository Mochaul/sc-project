import tkinter, configparser, random, os, tkinter.messagebox, tkinter.simpledialog

window = tkinter.Tk()

window.title("Tenggelamkan !")

#prepare default values

rows = 10
cols = 10
mines = 10

field = []
buttons = []

colors = ['#FFFFFF', '#0000FF', '#008200', '#FF0000', '#000084', '#840000', '#008284', '#840084', '#000000']

gameover = False
customsizes = []


# def createMenu():
#     menubar = tkinter.Menu(window)
#     menusize = tkinter.Menu(window, tearoff=0)
#     menusize.add_command(label="custom", command=setCustomSize)
#     menusize.add_separator()
#     for x in range(0, len(customsizes)):
#         menusize.add_command(label=str(customsizes[x][0])+"x"+str(customsizes[x][1])+" with "+str(customsizes[x][2])+" mines", command=lambda customsizes=customsizes: setSize(customsizes[x][0], customsizes[x][1], customsizes[x][2]))
#     menubar.add_cascade(label="about us", menu=menusize)
#     menubar.add_command(label="exit", command=lambda: window.destroy())
#     window.config(menu=menubar)
#




def prepareWindow():
    global rows, cols, buttons
    tkinter.Button(window, text="start").grid(row=0, column=0, columnspan=cols,
                                                sticky=tkinter.N + tkinter.W + tkinter.S + tkinter.E)
    tkinter.Button(window, text="Restart").grid(row=0, column=102, columnspan=cols, sticky=tkinter.N+tkinter.W+tkinter.S+tkinter.E)
    tkinter.Label(window, text="Mine").grid(row=1, column=0, columnspan=cols,
                                             sticky=tkinter.N + tkinter.W + tkinter.S + tkinter.E)
    tkinter.Label(window, text="Enemy").grid(row=1, column=101, columnspan=cols,
                                             sticky=tkinter.N + tkinter.W + tkinter.S + tkinter.E)
    buttons = []
    labels = []
    for x in range(0, rows):
        buttons.append([])
        labels.append([])
        for y in range(0, cols):
            b = tkinter.Button(window, text="", width=2)
            b.bind()
            b.grid(row=x+2, column=101+y, sticky=tkinter.N+tkinter.W+tkinter.S+tkinter.E)
            buttons[x].append(b)
            l = tkinter.Label(window, text="", width=2, relief="groove")
            l.grid(row=x + 2, column=y, sticky=tkinter.N + tkinter.W + tkinter.S + tkinter.E)
            labels[x].append(l)


    tkinter.Label(window, text= "kapal anda [  ] [  ] [  ] [  ] [  ] [  ]").grid(row=101, column=0, columnspan=cols, sticky=tkinter.N+tkinter.W+tkinter.S+tkinter.E)
    tkinter.Label(window, text="kapal lawan [  ] [  ] [  ] [  ] [  ] [  ]").grid(row=102, column=0, columnspan=cols,
                                                     sticky=tkinter.N + tkinter.W + tkinter.S + tkinter.E)



prepareWindow()
window.mainloop()