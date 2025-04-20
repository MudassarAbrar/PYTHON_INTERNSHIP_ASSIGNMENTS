# product.py

class Product:
    def __init__(self, product_id, name, quantity, price, category):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def update_price(self, new_price):
        self.price = new_price

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price,
            "category": self.category
        }
