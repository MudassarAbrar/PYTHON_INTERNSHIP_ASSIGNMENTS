# report_generator.py
import matplotlib.pyplot as plt

class ReportGenerator:
    def __init__(self, inventory):
        self.inventory = inventory

    def show_report(self):
        names = [p.name for p in self.inventory.products]
        quantities = [p.quantity for p in self.inventory.products]
        plt.bar(names, quantities, color="skyblue")
        plt.title("Inventory Stock Levels")
        plt.xlabel("Product Name")
        plt.ylabel("Quantity")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
