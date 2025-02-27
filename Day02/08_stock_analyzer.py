
"""  
Control Flow with Multiple Conditions
Time: 1.5-2 hours

Why: Complex decisions (like tiered discounts or stock alerts) need nested or multi-branch logic.

Learning Content
If-Elif-Else: Multiple conditions.

Example:
python
price = 120
if price > 100:
    print("Expensive")
elif price > 50:
    print("Moderate")
else:
    print("Cheap")

Nested If: Conditions inside conditions.


Create stock_analyzer.py in the same directory. Write a program that:

Asks for an item name, price (float), and quantity (int).

Applies a discount based on price:

100: 20% off

50: 10% off

≤ 50: No discount

Checks stock level:

If quantity < 5, print a “Low stock” warning.
Prints item details, final price, and stock status.
"""

item_name = input("Enter item name: ")
item_price = float(input("Enter item price: "))
stock_quantity = int(input("Enter stock quantity: "))

# Common sense check for negative values, item price and quantity must be non-negative
if item_price < 0 or stock_quantity < 0:
    print("Error: Price and quantity must be non-negative!")
    exit()

# applies a discount based on price
if item_price >= 100:
    discount = 20
    final_price = item_price * 0.8
elif item_price >= 50:
    discount = 10
    final_price = item_price * 0.9
else:
    discount = 0
    final_price = item_price

print(f"Item: {item_name} | Price: {item_price} | Quantity: {stock_quantity} | Discount: {discount}% | Final Price: {round(final_price, 2)}")

if stock_quantity <= 5:
    print("Warning: Low stock")