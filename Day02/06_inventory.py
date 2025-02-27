

"""  
Write a program that:

Asks for an item name (string).
Asks for its price (float).
Asks for stock quantity (int).
Sets a bool variable in_stock to True if quantity > 0, False otherwise.
Prints all details.
"""

item_name = input("Enter item name: ")
item_price = float(input("Enter item price: "))
stock_quantity = int(input("Enter stock quantity: "))

is_in_stock = stock_quantity > 0 # < 0 Not in stock, > 0 In stock
print(f"Item: {item_name} | Price: {item_price} | Quantity: {stock_quantity} | In Stock: {is_in_stock}")