from tkinter import *
from tkinter import messagebox

import utility
import main


class Login(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x125")
        self.title("Login")
        self.columnconfigure(1, weight=1)
        self.usertext = Label(text="ID:")
        self.pswdtxt = Label(text="PIN:")

        self.usr = Entry()
        self.pswd = Entry(show='*')

        self.usertext.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.pswdtxt.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.usr.grid(row=0, column=1, padx=50, pady=10)
        self.pswd.grid(row=1, column=1, padx=50, pady=10)

        self.loginbutton = Button(text="Login", command=self.login)
        self.loginbutton.grid(row=2, column=1, sticky="e", padx=10, pady=10)

    def login(self):
        username = self.usr.get()
        password = self.pswd.get()
        self.usr.delete(0, END)
        self.pswd.delete(0, END)
        user = utility.login_user(username, password)
        if user is None:
            messagebox.showerror(title="Fail", message="Failed to login")
        else:
            self.iconify()
            self.destroy()
            mainapp = main.MainApp(user[0])
            mainapp.mainloop()
            print(username)
            print(password)


app = Login()
app.mainloop()