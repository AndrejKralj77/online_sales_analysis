class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product, quantity):
        if product.quantity >= quantity:
            self.cart_items.append((product, quantity))
            product.quantity -= quantity
        else:
            print(f"Nema dovoljno proizvoda na stanju za {product.name}!")

    def calculate_total(self):
        return sum(product.price * quantity for product, quantity in self.cart_items)

    def display_cart(self):
        print("\nSadržaj korpe:")
        for product, quantity in self.cart_items:
            print(f"{product.name} - {quantity} kom - {product.price * quantity} RSD")
        print(f"Ukupna cena: {self.calculate_total()} RSD")
