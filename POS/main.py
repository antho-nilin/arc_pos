from tkinter import *
from tkinter import messagebox

import utility
import components


class MainApp(Tk):
    def __init__(self, username):
        super().__init__()
        self.userid = username
        self.title('POS')
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.topbar = TopBar(self)
        self.topbar.grid(column=0, row=0, columnspan=2, sticky='NEW')
        self.productlist = ProductList(self)
        self.productlist.grid(column=0, row=1, rowspan=2, sticky='NSEW')
        self.purchaselist = PurchaseList(self)
        self.purchaselist.grid(column=1, row=1, sticky='EW')
        self.paymentoptions = PaymentOptions(self)
        self.paymentoptions.grid(column=1, row=2, sticky='EW')
        self.currentpurchase = []
        self.bind("<Delete>", self.purchaselist.delete_item)

    def add_item(self, item_id):
        self.currentpurchase.append(item_id)
        self.purchaselist.add_item(item_id)

    def get_total_price(self):
        totalprice = 0
        for item in self.currentpurchase:
            totalprice = totalprice + utility.get_product_price(item)
        return totalprice

    def paywith(self, price):
        if len(self.currentpurchase) == 0:
            return
        elif price < self.get_total_price():
            messagebox.showerror('Invalid Amount', 'Error: Not Enough Money')
        else:
            self.topbar.updatepurchase(self.get_total_price())
            self.topbar.updatechange(price - self.get_total_price())
            self.purchaselist.clear_list()
            utility.insert_sale(self.currentpurchase, self.userid)
            self.currentpurchase = []

    def cancel_sale(self, event=None):
        self.purchaselist.clear_list()
        self.currentpurchase = []

    def delete_item(self, index):
        self.currentpurchase.pop(index)

    def cashpay(self, event=None):
        cashenter = components.CashEnter(self)


class TopBar(Frame):
    def __init__(self, main):
        super().__init__(master=main, bg="#ADD8E6")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.lastpurchase = Label(master=self, text="Last Purchase: ", bg="#ADD8E6")
        self.change = Label(master=self, text="Change: ", bg="#ADD8E6")
        self.lastpurchase.grid(row=0, column=0, ipadx=20, ipady=20)
        self.change.grid(row=0, column=1, ipadx=20, ipady=20)

    def updatepurchase(self, price):
        self.lastpurchase.config(text=("Last Purchase: %f" % price))

    def updatechange(self, price):
        self.change.config(text=("Change: %f" % price))


class ProductList(Frame):
    def __init__(self, main):
        self.main = main
        super().__init__(master=main, bg="red")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.categories = []
        self.products = []
        self.rownum = 0
        for category in utility.get_categories():
            new = CategoryButton(self, category)
            new.grid(column=self.rownum, row=0, padx=10, pady=10)
            self.categories.append(new)
            self.columnconfigure(self.rownum, weight=1)
            self.rownum += 1
        self.show_category(5)

    def show_category(self, category_id):
        print("showing %d" % category_id)
        for product in self.products:
            product.destroy()
        i = 0
        j = 1
        for product in utility.get_products(category_id):
            if i == self.rownum:
                i = 0
                j += 1
            new = ItemButton(self, product)
            new.grid(column=i, row=j, padx=10, pady=10)
            self.products.append(new)
            i += 1

    def add_item(self, item_id):
        self.main.add_item(item_id)


class PurchaseList(Frame):
    def __init__(self, main):
        self.main = main
        super().__init__(master=main, bg="green")
        self.scroll = Scrollbar(master=self)
        self.list = Listbox(master=self, height=35, width=50, yscrollcommand=self.scroll.set, font='TkDefaultFont 11')
        self.list.pack(side=LEFT, padx=20, pady=20)
        self.scroll.pack(side=LEFT, padx=20, pady=20, fill=Y)

    def add_item(self, item_id):
        newitem = utility.get_product(item_id)
        newstring = newitem[0].ljust(20) + str(newitem[1])
        print(len(newstring))
        self.list.insert(END, newstring)

    def clear_list(self):
        self.list.delete(0, END)

    def delete_item(self, event=None):
        print("sdsds")
        for i in self.list.curselection():
            print(i)
            self.list.delete(i)
            self.main.delete_item(i)


class PaymentOptions(Frame):
    def __init__(self, main):
        self.main = main
        super().__init__(master=main, bg="purple")
        self.fifty = Label(master=self, text="$50", height=5, width=30, bg="yellow")
        self.fifty.grid(row=0, column=0, padx=20, pady=20)
        self.fifty.bind("<Button-1>", self.fiftypay)
        self.twenty = Label(master=self, text="$20", height=5, width=30, bg="yellow")
        self.twenty.grid(row=0, column=1, padx=20, pady=20)
        self.twenty.bind("<Button-1>", self.twentypay)
        self.ten = Label(master=self, text="$10", height=5, width=30, bg="yellow")
        self.ten.grid(row=1, column=0, padx=20, pady=20)
        self.ten.bind("<Button-1>", self.tenpay)
        self.five = Label(master=self, text="$5", height=5, width=30, bg="yellow")
        self.five.grid(row=1, column=1, padx=20, pady=20)
        self.five.bind("<Button-1>", self.fivepay)
        self.cash = Label(master=self, text="CASH", height=5, width=30, bg="yellow")
        self.cash.grid(row=2, column=0, padx=20, pady=20)
        self.cash.bind("<Button-1>", self.main.cashpay)
        self.eftpos = Label(master=self, text="EFTPOS", height=5, width=30, bg="yellow")
        self.eftpos.grid(row=2, column=1, padx=20, pady=20)
        self.eftpos.bind("<Button-1>", self.eftpospay)
        self.cancel = Label(master=self, text="Cancel Sale", height=5, width=30, bg="yellow")
        self.cancel.grid(row=0, column=2, padx=20, pady=20)
        self.cancel.bind("<Button-1>", self.main.cancel_sale)

    def eftpospay(self, event=None):
        self.main.paywith(self.main.get_total_price())

    def fivepay(self, event=None):
        self.main.paywith(5)

    def tenpay(self, event=None):
        self.main.paywith(10)

    def twentypay(self, event=None):
        self.main.paywith(20)

    def fiftypay(self, event=None):
        self.main.paywith(50)


class ItemButton(Label):
    def __init__(self, main, item):
        super().__init__(master=main, text=item[1], height=8, width=20, bg="green")
        self.main = main
        self.itemid = item[0]
        self.bind("<Button-1>", self.add_item)

    def add_item(self, event=None):
        self.master.add_item(self.itemid)


class CategoryButton(Label):
    def __init__(self, main, category):
        self.master = main
        self.categoryid = category[0]
        super().__init__(master=main, text=category[1], height=8, width=20, bg="blue")
        self.bind("<Button-1>", self.switch_category)

    def switch_category(self, event=None):
        self.master.show_category(self.categoryid)


print('test')
