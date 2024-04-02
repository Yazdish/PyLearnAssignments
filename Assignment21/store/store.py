import sqlite3

def show_menu():
    print("1-show list")
    print("2-add new product")
    print("3-edit a product")
    print("4-remove a product")

def load_database():
    global connection
    global my_cursor
    connection = sqlite3.connect("store.db")
    my_cursor = connection.cursor()

def show_list():
    result = my_cursor.execute("SELECT * FROM products")
    all_products = result.fetchall()
    for product in all_products:
        print(product)

def add_new():
    new_product_name = input("enter the NAME of product you'd like to add: ")
    new_product_price = int(input("enter the PRICE of new product: "))
    new_product_count = int(input("enter the COUNT of the new product: "))
    my_cursor.execute(f"INSERT INTO products(name, price, count) VALUES ('{new_product_name}','{new_product_price}','{new_product_count}')")
    connection.commit()
    print("New product Added!\n")

def edit():
    name = input("Which product you want to edit: ")
    which = input("Which property do U want to edit(name, price, count): ")
    if which == "name":
        new = input("enter new name: ")
        my_cursor.execute(f"UPDATE products SET {which} = '{new}' WHERE name = '{name}'")
        connection.commit()
        print("Name changed successfuly!\n")
    elif which == "price" or which == "count":
        new = int(input("enter new information: "))
        my_cursor.execute(f"UPDATE products SET {which} = {new} WHERE name = '{name}'")
        connection.commit()
        print("Done!\n")

def remove():
    name = input("enter the NAME of product you want to remove: ")
    my_cursor.execute(f"DELETE FROM products WHERE name ='{name}'")
    connection.commit()
    print("item removed successfully!\n")

load_database()
while True:
    show_menu()
    choice = int(input())
    if choice == 1:
        show_list()
    elif choice == 2:
        add_new()
    elif choice == 3:
        edit()
    elif choice == 4:
        remove()
