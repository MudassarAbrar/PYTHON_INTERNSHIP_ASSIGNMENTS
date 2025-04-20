
# inventory.py
import json
import csv
from product import Product

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def sort_by_quantity(self):
        return sorted(self.products, key=lambda x: x.quantity)

    def sort_by_category(self):
        return sorted(self.products, key=lambda x: x.category)

    def export_to_csv(self):
        with open("inventory_export.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Quantity", "Price", "Category"])
            for p in self.products:
                writer.writerow([p.product_id, p.name, p.quantity, p.price, p.category])

    def save_to_file(self):
        with open("inventory_data.txt", "w") as f:
            json.dump([p.to_dict() for p in self.products], f)

    def load_from_file(self):
        try:
            with open("inventory_data.txt", "r") as f:
                data = json.load(f)
                self.products = [Product(**item) for item in data]
        except FileNotFoundError:
            self.products = []
