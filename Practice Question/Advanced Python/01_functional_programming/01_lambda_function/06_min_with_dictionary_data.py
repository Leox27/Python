"""
#6. min() with Dictionary Data
products = [
    {"name": "Laptop", "price": 75000},
    {"name": "Mouse", "price": 1200},
    {"name": "Keyboard", "price": 2500},
    {"name": "Monitor", "price": 15000}
]

Use min() with a lambda function to find and print the product with the lowest price.
Don't use a loop.
"""

products = [
    {"name": "Laptop", "price": 75000},
    {"name": "Mouse", "price": 1200},
    {"name": "Keyboard", "price": 2500},
    {"name": "Monitor", "price": 15000}
]

lowest_price = min(products, key=lambda x: x["price"])
print(lowest_price)
'''
{'name': 'Mouse', 'price': 1200}
'''
