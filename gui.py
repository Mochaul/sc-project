import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3

TOP = "ABCDEFGHIJ"
SIDE = "0123456789"

class gui(tk.Tk):

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

        label_0 = tk.Label(self, text="WELCOME TO TENGGELAMKAN !", font=("bold", 15))
        label_11 = tk.Label(self, text="Format penulisan X sampai X (misal A4 sampai A9)", font=("bold", 10))
        label_0.place(x=70, y=53)
        label_11.place(x=90, y=100)
        self.board = 100 * [" "]
        label_1 = tk.Label(self, text="Martadinata (5)", width=20, font=("bold", 10))
        label_1.place(x=80, y=130)
        label_2 = tk.Label(self, text="Kapal Fatahilah (4)", width=20, font=("bold", 10))
        label_2.place(x=68, y=180)
        label_3 = tk.Label(self, text="Kapal Cakra (3)", width=20, font=("bold", 10))
        label_3.place(x=70, y=230)
        label_4 = tk.Label(self, text="Kapal Boa (3)", width=20, font=("bold", 10))
        label_4.place(x=70, y=280)
        label_5 = tk.Label(self, text="Kapal Andau (2)", width=20, font=("bold", 10))
        label_5.place(x=85, y=330)
        label6 = tk.Label(self, text=self.render())
        label6.place(x = 80, y = 430)

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
        self.button2 = tk.Button(self, text="next", command= lambda : controller.show_frame("PageOne"))
        self.button.place(x=130, y = 380)
        self.button2.place(x= 240, y = 380)



    def on_button(self):
        pos_1 = self.entry_1.get()
        pos_2 = self.entry_2.get()
        pos_3 = self.entry_3.get()
        pos_4 = self.entry_4.get()
        pos_5 = self.entry_5.get()
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
            print ("true")
            arrship1 = ["martadinata", 5, pos_1]
            arrship2 = ["fatahilah", 4, pos_2]
            arrship3 = ["cakra", 3, pos_3]
            arrship4 = ["boa", 3, pos_4]
            arrship5 = ["andau", 2, pos_5]
            arrall = [arrship1,arrship2,arrship3,arrship4,arrship5]
            return arrall


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
        label2 = tk.Label(left, text="Anda")
        self.text_tembak = tk.StringVar(self)
        button1 = tk.Button(left, text="Get", command=self.on_button)
        self.entry8 = tk.Entry(left, textvariable = self.text_tembak)
        label15 = tk.Label(left, text= self.render())
        label3 = tk.Label(right, text="Lawan")
        label14 = tk.Label(right, text=self.render())

        left.pack(side="left", expand=True, fill="both")
        right.pack(side="right", expand=True, fill="both")
        label2.pack()
        self.entry8.pack()
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
        pos = self.entry8.get()
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
        print(self.entry8.get())
        self.entry8.delete(0, 'end')



if __name__ == "__main__":
    app = gui()
    app.mainloop()

