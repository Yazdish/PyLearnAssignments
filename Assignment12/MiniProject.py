from actors import Actor
from film import Film
from series import Series
from clip import Clip
from documentary import Documentary
from media import Media

class Product:
    def __init__(self, i, n, p, c):
        self.id = i
        self.name = n
        self.price = p
        self.count = c

    @staticmethod
    def add():
        code = input("Enter Code: ")
        name = input("Enter Name: ")
        price = input("Enter Price: ")
        count = input("Enter Count: ")
        new_product = Product(code, name, price, count)
        PRODUCTS.append(new_product)

    def edit(self):
        user_input = int(input("Enter Code: "))
        for product in PRODUCTS:
            if product["code"] == user_input:
                while True:
                    print("Select What to Edit: ")
                    print("1- Name")
                    print("2- Price")
                    print("3- Count")
                    choice = int(input("Enter Number: "))
                    if choice == 1:
                        new_name = input("Enter New Name: ")
                        product["name"] = new_name
                        break
                    elif choice == 2:
                        new_price = input("Enter New Price: ")
                        product["price"] = new_price
                        break
                    elif choice == 3:
                        new_count = input("Enter New Count: ")
                        product["count"] = new_count
                        break
                    else:
                        print("mese adam vared kon :|")
                print("PRODUCT Edit Successfully..")
                break
        else:
            print("not found")

    @staticmethod
    def search():
        print("1-Search With Name_filem id ")
        print("2-Search With Duration ")
        choice=int(input("Which Method do You Want to Search : "))
        if choice==1:
            userKey=input("Pls Enter Media Id : " )
            f=0
            for i in range(len(PRODUCTS)):
                if str(PRODUCTS[i]['id'])==userKey or (PRODUCTS[i]['name_filem'].lower()==userKey.lower()) :
                    print(PRODUCTS[i])
                    f=1
            if f==0:   
                print("Media Not Found!")
        elif choice==2:
            print("Duration between A and B ")
            A=int(input("A : "))
            B=int(input("B : "))
            f=0
            for i in range(len(PRODUCTS)):
                if PRODUCTS[i]["duration"]>=A and PRODUCTS[i]["duration"]>=B :
                    print(PRODUCTS[i])
                    f=1
            if f==0:   
                print("Media Not Found!")      

        else:
            print('Try Again !')

    def remove(self):
        A = 0
        id = input("enter id: ")
        for product in PRODUCTS:
                code_a = A + 1
                if product["id"] == id:
                    del PRODUCTS[A-1]
                    print("Your item has been successfully deleted")
                    break
                else:
                    print("not found")

    @staticmethod
    def show_list():
        print("id\t\t name_filem\t\t\t duration")
        for product in PRODUCTS:
            print(Media["id"],"\t\t",product["name_filem"],product["duration"])    

    def download(self):
        Media.download()

PRODUCTS = []

def read_from_database():
    f = open("G:/Python/PyLearn7/Assignment12/txt_media.txt", "r")
    for line in f:
        result = line.split(",")
        # my_dict = {"code": result[0], "name": result[1], "price": result[2], "count": result[3]}
        my_obj = Product(result[0],result[1],result[2],result[3])
        PRODUCTS.append(my_obj)
    f.close

def write_to_database():
    f = open("G:/Python/PyLearn7/Assignment12/txt_media.txt", "w")
    for product in PRODUCTS:
        f.write(f"{product['code']},{product['name']},{product['price']},{product['count']}\n")
    f.close()
  
def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- Show List")
    print("6- Download")
    print("7- TBD")
    print("8- Exit")

print("Welcome to DI$H MEDIA")
print("Loading...")
read_from_database()
print("Data loaded.")



while True:
    show_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        Product.add()
    
    elif choice == 2:
        id = int(input("enter product id:"))
        for product in PRODUCTS:
            if product.id == id:
                product.edit()
    
    elif choice == 3:
        id = int(input("enter product id: "))
        for p in PRODUCTS:
            if p.id == id:
                p.remove()
    
    elif choice == 4:
        Product.search()
    
    elif choice == 5:
        Product.show_list()
    
    elif choice == 6:
        Media.download()
    
    elif choice == 7:
        print("Coming Soon!")
    
    elif choice == 8:
        write_to_database()
    
        exit(0)
    else:
        print("mese adam vared kon :|")