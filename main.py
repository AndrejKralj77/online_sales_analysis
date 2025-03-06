from product_manager import ProductManager
from product import Product

# Kreiranje instanci ProductManager i nekoliko proizvoda
manager = ProductManager()
product1 = Product("Laptop", 80000, 5)
product2 = Product("Telefon", 50000, 10)
product3 = Product("Miš", 2000, 15)

# Dodavanje proizvoda u inventar
manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

# Prikaz proizvoda i ukupne vrednosti
print("Inventar proizvoda:")
manager.display_products()
print(f"Ukupna vrednost inventara: {manager.total_inventory_value()} RSD")
