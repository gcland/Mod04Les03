class Product:
    def __init__(self, product_id, name, price):
        self.__product_id = product_id
        self.__name = name
        self.__price = price

    def get_product_id(self):
        print(f"Product ID:{self.__product_id}.")
    
    def get_name(self):
        print(f"Name: {self.__name}.")
    
    def get_price(self):
        print(f"Price: ${self.__price}.") 
    
inventory = {}
book = Product("001", "1984", 9.99)

book.get_product_id()
book.get_name()
book.get_price()
