from product import Product
from product_manager import ProductManager
from cart import Cart


# Kreiranje instanci ProductManager i nekoliko proizvoda
manager = ProductManager()
product1 = Product("Pametni telefon", 55000, 4)
product2 = Product("Gaming laptop", 130000, 2)
product3 = Product("Bežične slušalice", 6000, 8)


# Kreiranje ProductManager i dodavanje proizvoda
product_manager = ProductManager()
product1 = Product("Telefon", 50000, 5)
product2 = Product("Laptop", 120000, 3)
product3 = Product("Slusalice", 5000, 10)


product_manager.add_product(product1)
product_manager.add_product(product2)
product_manager.add_product(product3)

# Kreiranje korpe i dodavanje proizvoda
cart = Cart()
cart.add_to_cart(product1, 1)
cart.add_to_cart(product2, 2)
cart.add_to_cart(product3, 1)

# Prikaz sadržaja korpe
cart.display_cart()

