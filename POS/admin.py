import sqlite3
from sqlite3 import Error
from tkinter import *

try:
    connection = sqlite3.connect("pos.db")
    print("Connection to SQLite DB successful")
except Error as e:
    print(f"The error '{e}' occurred")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def test(event):
    print('works')


window = Tk()
window.title("Admin")
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

sidebar = Frame(master=window, borderwidth=1, bg="#ADD8E6")
sidebar.grid(row = 0, column = 0, sticky = "nsw")
sidebar.bind("<Button-1>", test)

productslabel = Label(master=sidebar, text="Products", bg="#ADD8E6")
categorieslabel = Label(master=sidebar, text="Categories", bg="#ADD8E6")
analytics = Label(master=sidebar, text="Analytics", bg="#ADD8E6")
refunds = Label(master=sidebar, text="Refunds", bg="#ADD8E6")
earnings = Label(master=sidebar, text="Earnings", bg="#ADD8E6")
sessions = Label(master=sidebar, text="Sessions", bg="#ADD8E6")
employees = Label(master=sidebar, text="Employees", bg="#ADD8E6")
productslabel.pack(ipadx=20, ipady=20)

categorieslabel.pack(ipadx=20, ipady=20)
analytics.pack(ipadx=20, ipady=20)
refunds.pack(ipadx=20, ipady=20)
earnings.pack(ipadx=20, ipady=20)
sessions.pack(ipadx=20, ipady=20)
employees.pack(ipadx=20, ipady=20)
window.mainloop()