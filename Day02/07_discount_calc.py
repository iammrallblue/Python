

"""
Write a program that:

Asks for an item price (float).
Asks for a discount percentage (float, e.g., 20 for 20%).
Calculates the discounted price (price - price * discount/100).
Checks if the discounted price is “reasonable” (greater than 0 and less than original price).
Prints original price, discount amount, and final price.
"""

item_price = float(input("Enter item price: "))
discount_percentage = float(input("Enter discount percentage: "))

# show the discount amount
discount_amount = item_price * discount_percentage / 100

final_price = item_price - discount_amount

# Check if the discounted price is reasonable
is_reasonable = final_price > 0 and final_price < item_price

print(f"Original Price: {item_price} | Discount Amount: {discount_amount} | Final Price: {final_price} | Reasonable: {is_reasonable}")

amount_saved = item_price - final_price
print(f"You have saved: {amount_saved}")