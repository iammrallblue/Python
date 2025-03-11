
"""  
Day 4 - Part 2: Dictionaries
File: Create cart_dict.py/16_dictionaries.py.

Why: Dictionaries use key-value pairs (e.g., "name": "S Condom")—a step closer to real data structures like Django models.

Key Knowledge Points

What’s a Dictionary?:
A collection of key-value pairs: {"name": "S Condom", "price": 6.99}.

Access: item["name"] → "S Condom".

Why Use It?:
Unlike sublists ([name, price]), keys make data explicit—no guessing item[0] vs. item[1].

E-commerce: Models a product with attributes (name, price, quantity).

Operations:
Add: cart["name"] = "S Condom".

Loop: for key, value in cart.items():.

Task: Dictionary-Based Cart

Write a program that:

Uses a list of dictionaries to store 3 items (name, price).

Validates price input.

Prints the cart and total cost.

Q: please explain this item["name"] = input(f"Add item {i + 1} name: ") # add name to the dictionary A: 

"""

# Start with an empty cart
cart = [] # list of dictionaries to store items

for i in range(3): 
    item = {} # create an empty dictionary for the item
    item["name"] = input(f"Add item {i + 1} name: ") # add name to the dictionary
    while True:
        try:
            item["price"] = float(input(f"Add item {i + 1} price: "))
            if item["price"] < 0:
                print("Price must be positive.")
                continue
            break
        except ValueError:
            print("Price must be a number. Try again.")
    
    cart.append(item) # add the item to the cart

print("Your Cart:", cart)
#Your Cart: [{'name': 'S Condom', 'price': 6.99}, {'name': 'M Condom', 'price': 7.99}, {'name': 'L Condom', 'price': 9.99}]

# calculate the total and display the cart
total_cost = 0
print("Your Cart:")
for item in cart:
    print(f"{item['name']}: ${item['price']}")
    total_cost += item["price"]

print(f"Total cost: ${round(total_cost,2)}")