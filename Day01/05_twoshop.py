


"""  
Task: twoshop.py
Write a program that:
Asks for two items (name, price, quantity for each).
Calculates the total (price1 * qty1 + price2 * qty2).
Applies a 15% discount if total > 100.
Prints both items and the final total.
"""

item1 = input("Enter first item name: ")
price1 = float(input("Enter first item price: "))
quantity1 = int(input("Enter first item quantity: "))

item2 = input("Enter second item name: ")
price2 = float(input("Enter second item price: "))
quantity2 = int(input("Enter second item quantity: "))

total = price1 * quantity1 + price2 * quantity2
if total > 100:
    print("You spent more than 100, applying 15% discount.")
    total = total * 0.85

print("Item 1:", item1, "Item 2:", item2, "Final price is:", total)
