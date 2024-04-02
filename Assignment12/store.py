class Product:
    def __init__(self, i, n, p, c):
        self.id = i
        self.name = n 
        self.price = p
        self.count = c

    @staticmethod
    def add():
        id = int(input("enter id: "))
        name = input("enter name: ")
        price = int(input("enter price: "))
        count = int(input("enter count: "))
        new_product = Product(id, name, price, count)
        PRODUCTS.append(new_product)

    def edit(self):
        ...

    @staticmethod
    def search(self):
        ...
    
    def remove(self):
        ...

    @staticmethod
    def show_list():
        print("code\t\tname\t\tprice\t\tcount")
        for product in PRODUCTS:
            print(product.id, "\t\t" ,product.name , "\t\t", product.price, "\t\t", product.count )

    def show_info(self):
        ...
    

PRODUCTS = []

def read_from_database():
    f = open("G:/Python/PyLearn7/Assignment7/database.txt", "r")
    for line in f:
        result = line.split(",")
        my_obj = Product(result[0], result[1], result[2], result[3])
        PRODUCTS.append(my_obj)
    f.close

def write_to_database():
    f = open("G:/Python/PyLearn7/Assignment7/database.txt", "w")
    for product in PRODUCTS:
        f.write(str(product.id)+","+str(product.name)+","+str(product.price)+","+str(product.count)+"\n")
    print("succesfully saved!")
    f.close()


def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- Show List")
    print("6- Buy")
    print("7- QR Code")
    print("8- Exit")


print("Welcome to YAZDISH Store")
print("Loading...")
read_from_database()
print("Data loaded.")

while True:
    show_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        Product.add()
    
    elif choice == 2:
        id = int(input("enter id: "))
        for product in PRODUCTS:
            if product.id == id:
                product.edit()
    
    elif choice == 3:
        id = int(input("enter id: "))
        for product in PRODUCTS:
            if product.id == id:
                product.remove()

    
    elif choice == 4:
        Product.search()
    
    elif choice == 5:
        Product.show_list()
    
    elif choice == 6:
        print("TROLL")
    
    elif choice == 7:
        print("yeah you wish!")
    
    elif choice == 8:
        write_to_database()
        exit(0)
    
    else:
        print("mese adam vared kon :|")
    
