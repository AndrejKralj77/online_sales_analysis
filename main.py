from product_manager import ProductManager
from product import Product

# Kreiranje instanci ProductManager i nekoliko proizvoda
manager = ProductManager()
product1 = Product("Pametni telefon", 55000, 4)
product2 = Product("Gaming laptop", 130000, 2)
product3 = Product("Bežične slušalice", 6000, 8)


# Dodavanje proizvoda u inventar
manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

# Prikaz proizvoda i ukupne vrednosti
print("Inventar proizvoda:")
manager.display_products()
print(f"Ukupna vrednost inventara: {manager.total_inventory_value()} RSD")
