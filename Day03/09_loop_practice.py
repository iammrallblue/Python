


"""  
Part 1: Loops (for and while)

Why: Loops process multiple items—like listing products or calculating totals.

Learning Content
for Loop: Repeats over a sequence.

Example: for i in range(3): print(i) → 0, 1, 2.

With lists: items = ["apple", "banana"]; 

for item in items: print(item).

while Loop: Repeats until a condition is false.

Example: count = 0; while count < 3: print(count); count += 1.

Task 1: Multi-Item Entry

Create multi_items.py Write a program that:

Asks how many items to enter.

Loops to collect each item’s name and price.

Prints all items with a numbered list.
"""

# Ask how many items to enter
number_of_items = int(input("How many items do you want to enter? "))

# Loop to collect each item's name and price depending on the number of items
for i in range(number_of_items):
    item_name = input(f"Enter item {i + 1} name: ")
    item_price = float(input(f"Enter item {i + 1} price: "))
    print(f"{i + 1}. {item_name} - ${item_price}")
    