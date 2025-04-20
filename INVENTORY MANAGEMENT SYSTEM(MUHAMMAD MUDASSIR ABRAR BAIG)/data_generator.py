
'''Args:
    num_products: The number of product data entries to generate.

Returns:
    A list of dictionaries, where each dictionary represents a product.'''

import random
import string
import json

categories = ["Electronics", "Stationery", "Furniture", "Cosmetics", "Clothing", "Books", "Kitchenware", "Toys", "Sports", "Tools"]
product_names = ["Laptop", "Keyboard", "Mouse", "Pen", "Pencil", "Chair", "Table", "Foundation", "Blush", "Shirt", "Dress", "Novel", "Cookbook", "Plate", "Spoon", "Doll", "Car", "Basketball", "Tennis Racket", "Hammer", "Saw"]
products = []

for _ in range(500):
    product_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    name = random.choice(product_names)
    quantity = random.randint(1, 500)
    price = round(random.uniform(10, 2000), 2)
    category = random.choice(categories)

    product = {
        "product_id": product_id,
        "name": name,
        "quantity": quantity,
        "price": price,
        "category": category
    }
    products.append(product)
print (products)


with open("DATA CONTENT/inventory_data.txt", "w") as file:
    import random
import string
import json  # Import json to write the list properly

categories = ["Electronics", "Stationery", "Furniture", "Cosmetics", "Clothing", "Books", "Kitchenware", "Toys", "Sports", "Tools"]
product_names = ["Laptop", "Keyboard", "Mouse", "Pen", "Pencil", "Chair", "Table", "Foundation", "Blush", "Shirt", "Dress", "Novel", "Cookbook", "Plate", "Spoon", "Doll", "Car", "Basketball", "Tennis Racket", "Hammer", "Saw"]
products = []

for _ in range(500):
    product_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    name = random.choice(product_names)
    quantity = random.randint(1, 500)
    price = round(random.uniform(10, 2000), 2)
    category = random.choice(categories)

    product = {
        "product_id": product_id,
        "name": name,
        "quantity": quantity,
        "price": price,
        "category": category
    }
    products.append(product)



with open("inventory_data.txt", "w") as file:
    json.dump(products, file, indent=4)

print("Data has been written to inventory_data.txt successfully!")
