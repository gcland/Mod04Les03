class Product:
    def __init__(self, product_id, name, price):
        self.__product_id = product_id
        self.__name = name
        self.__price = price

    def get_product_id(self):
        print(f"Product ID: {self.__product_id}")
    
    def get_name(self):
        print(f"Name: {self.__name}")
    
    def get_price(self):
        print(f"Price: ${self.__price}") 

class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def get_author(self):
        print(f"Author name: {self.author}")

    def get_price(self, price):
        print(f"Discount price: ${price}") 

    def display_info(self):
        book.get_product_id()
        book.get_name()
        book.get_price(5.99)
        book.get_author()

class Electronics(Product):
    def __init__(self, product_id, name, price, battery_life, resolution):
        super().__init__(product_id, name, price)
        self.battery_life = battery_life
        self.resolution = resolution

    def get_battery_life(self):
        print(f"Battery life of device: {self.battery_life}")

    def get_resolution(self):
        print(f"Camera resolution of device: {self.resolution}")

    def get_price(self, price):
        print(f"Discount price: ${price}") 

    def display_info(self):
        electronics.get_product_id()
        electronics.get_name()
        electronics.get_price(299.99)
        electronics.get_battery_life()
        electronics.get_resolution()

class Clothing(Product):
    def __init__(self, product_id, name, price, clothing_size):
        super().__init__(product_id, name, price)
        self.clothing_size = clothing_size

    def get_clothing_size(self):
        print(f"Size of product: {self.clothing_size}")

    def get_price(self, price):
        print(f"Discount price: ${price}") 

    def display_info(self):
        clothing.get_product_id()
        clothing.get_name()
        clothing.get_price(29.99)
        clothing.get_clothing_size()

book = Book("001", "1984", 9.99, "George Orwell")
electronics = Electronics("002", "Drone", 499.99, "60 minutes", "4K")
clothing = Clothing("003", "T-Shirt", 49.99, "Large")

print("Book details:")
book.display_info()
print()
print("Electronic details:")
electronics.display_info()
print()
print("Clothing details:")
clothing.display_info()
