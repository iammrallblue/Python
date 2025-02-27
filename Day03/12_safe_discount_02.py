


"""  
Retry Logic

Task: Safe Discount Calculator
Write a new program that:

Reuses your apply_discount function.
Asks for price and discount percentage.
Uses try/except to catch invalid inputs.
Prints the result or an error message.
"""

def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# function takes in price and percentage as arguments and returns the discounted price
def apply_discount(price, percentage):
    discount = price * percentage / 100
    return round(price - discount, 2)

item_price = get_valid_input("Enter item price: ")
discount_percentage = get_valid_input("Enter discount percentage: ")
final_price = apply_discount(item_price, discount_percentage)
discounted_price = round(item_price - final_price, 2)
print(f"Original Price: {item_price} | Discount Amount: {discounted_price} | Final Price: {final_price}")