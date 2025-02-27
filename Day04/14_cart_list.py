
"""  
Day 3: Part 4 - Lists
File: Create cart_list.py.

Why: Lists manage collections of data (e.g., a shopping cart with multiple items)—a foundational skill for Django models later.

Learning Content

What’s a List?: An ordered, mutable collection of items.
Syntax: items = ["apple", "banana"].

Key Operations:
Access: items[0] → "apple" (index starts at 0).
Add: items.append("orange") → ["apple", "banana", "orange"].
Remove: items.remove("banana") → ["apple", "orange"].
Length: len(items) → Number of items.
Looping: Use for to iterate:
for item in items: print(item) → Prints each item.

Task: Shopping Cart List

Write a program that:

Starts with an empty cart (list).
Asks the user to add 3 items (name only for simplicity).
Prints the full cart and its total item count.
"""

# Start with an empty cart
cart = [] # Empty list to store items

# Ask the user to add 3 items
for i in range(3):
    item = input(f"Add item {i + 1}: ")
    cart.append(item) # Add item to the cart list