from tkinter import *
from tkinter import messagebox


class CashEnter(Tk):
    def __init__(self, mainwindow):
        super().__init__()
        self.title("Enter Cash")
        self.amount = Label(master=self, text="AMOUNT: ", font='TkDefaultFont 11')
        self.amount.pack(fill=X)
        self.mainwindow = mainwindow
        self.topbuttons = Frame(master=self)
        self.midbuttons = Frame(master=self)
        self.botbuttons = Frame(master=self)
        self.buttons = []
        i = 0
        while i < 4:
            new = NumberButton(self.topbuttons, self, str(i))
            new.pack(expand=True, fill=BOTH, side=LEFT, padx=5, pady=5)
            self.buttons.append(new)
            i += 1
        while i < 8:
            new = NumberButton(self.midbuttons, self, str(i))
            new.pack(expand=True, fill=BOTH, side=LEFT, padx=5, pady=5)
            self.buttons.append(new)
            i += 1
        while i < 10:
            new = NumberButton(self.botbuttons, self, str(i))
            new.pack(expand=True, fill=BOTH, side=LEFT, padx=5, pady=5)
            self.buttons.append(new)
            i += 1
        self.enter = NumberButton(self.botbuttons, self, ".")
        self.enter.pack(expand=True, fill=BOTH, side=LEFT, padx=5, pady=5)
        self.clear = Label(self.botbuttons, text="CLEAR", height=10, width=10, bg="grey")
        self.clear.pack(expand=True, fill=BOTH, side=LEFT, padx=5, pady=5)
        self.topbuttons.pack()
        self.midbuttons.pack()
        self.botbuttons.pack()
        self.bind("<Return>", self.enter_amount)

    def add_number(self, number):
        newtext = self.amount["text"] + number
        self.amount.config(text = newtext)

    def enter_amount(self, event=None):
        numberstring = self.amount["text"].split()
        if len(numberstring) == 2:
            self.mainwindow.paywith(float(numberstring[1]))
        self.destroy()


class NumberButton(Label):
    def __init__(self, main, master, number):
        super().__init__(master=main, text=number, height=10, width=10, bg="grey")
        self.number = number
        self.main = main
        self.master = master
        self.bind("<Button-1>", self.onclick)

    def onclick(self, event=None):
        self.master.add_number(self.number)
