

"""  
Day 4 - Part 3: Combining Lists, Dictionaries, and Functions
File: Create shop_cart.py.

Why: Tie together what you’ve learned (loops, functions, dictionaries) into a mini-shop—closer to real project logic.

Key Knowledge Points

Integration:
Lists hold multiple dictionaries (cart items).
Functions process data (e.g., calculate totals).

Practicality:
Simulates adding items and summarizing a cart—core e-commerce tasks.

Limitations:
Still memory-only—Django will add persistence later.

Task: Mini Shop Cart

Write a program that:
Defines a function to add items to the cart.

Collects 3 items (name, price) with validation.

Prints the cart and total with a function.
"""

# Define a function to add items to the cart
def add_item(cart):
    print("Type of cart: ", type(cart)) # Check type of cart
    item = {} # Create an empty dictionary
    item["name"] = input(f"Enter the item {len(cart) + 1} name: ") # Get the item name from the user
    while True:
        try:
            item["price"] = float(input(f"Enter the item {len(cart) + 1} price: ")) # Get the item price from the user
            if item["price"] < 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid price.")
    cart.append(item) # Add the item to the cart "list"
    
def print_cart(cart):
    total = 0
    print("Your cart: ")
    for i, item in enumerate(cart, 1):
        print(f"{i}: {item['name']}: ${item['price']}")
        total += item["price"]
    print(f"Total: ${round(total,2)}")
    
    
# Main program
cart = [] # Create an empty list
print("Type of cart before: ", type(cart)) # Check type of cart
for _ in range(3):
    add_item(cart)

print_cart(cart)