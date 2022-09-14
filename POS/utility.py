import sqlite3
import datetime

def login_user(username, password):
    con = sqlite3.connect("pos.db")
    info = {"username": username, "password": password}
    cursor = con.execute("SELECT * FROM employees WHERE username='%s' and password=%d" % (username, int(password)))
    print("SELECT employee_id FROM employees WHERE username='%s' and password=%d" % (username, int(password)))
    return cursor.fetchone()


def add_user(username, password):
    con = sqlite3.connect("pos.db")
    cursor = con.execute("INSERT INTO employees(username, password) VALUES('%s', %s)" % (username, password))
    con.commit()
    con.close()


def delete_user(employee_id):
    con = sqlite3.connect("pos.db")
    cursor = con.execute("DELETE FROM employees WHERE employee_id = %d", employee_id)
    con.commit()
    con.close()


def get_categories():
    con = sqlite3.connect("pos.db")
    cursor = con.execute("SELECT category_id, category_name FROM categories")
    return cursor.fetchall()


def get_products(category_id):
    con = sqlite3.connect("pos.db")
    cursor = con.execute("SELECT * FROM products WHERE category_id = %d" % category_id)
    return cursor.fetchall()


def get_product(item_id):
    con = sqlite3.connect("pos.db")
    cursor = con.execute("SELECT product_name, product_price FROM products WHERE product_id = %d" % item_id)
    return cursor.fetchone()


def get_product_price(item_id):
    con = sqlite3.connect("pos.db")
    cursor = con.execute("SELECT product_price FROM products WHERE product_id = %d" % item_id)
    return cursor.fetchone()[0]


def insert_sale(items, user_id):
    con = sqlite3.connect("pos.db")
    cursor = con.execute("INSERT INTO sales(datetime, sold_by) VALUES('%s', %s) RETURNING sale_id" % (datetime.datetime.now().strftime("%c"), user_id))
    print(datetime.datetime.now().strftime("%c"))
    cur_sale_id = cursor.fetchone()[0]
    print(cur_sale_id)
    for item in items:
        cursor = con.execute("INSERT INTO sold_items(sale_id, product_id) VALUES(%d, %d)" % (cur_sale_id, item))
    con.commit()
    con.close()


def get_sale(sale_id):
    con = sqlite3.connect("pos.db")
    cursor = con.execute("SELECT product_id from sold_items WHERE sale_id = %d" % sale_id)
    return cursor.fetchall()

