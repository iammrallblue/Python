
"""  
Exception Handling

File: Create safe_discount.py.

Why: Prevents your program from crashing when users enter invalid data (e.g., "abc" instead of a number)—crucial for a robust e-commerce app.

Learning Content

try/except: Catches errors so your program can handle them gracefully.
Syntax:

try:
    # Code that might fail
    num = int(input("Enter a number: "))
except ValueError:
    # What to do if it fails
    print("That’s not a number!")

ValueError: Happens when converting strings to numbers fails (e.g., float("abc")).

Why It Matters: In discount_func.py, if someone typed "xyz" for price, it crashed. Exceptions fix that.

Task: Safe Discount Calculator
Write a new program that:

Reuses your apply_discount function.
Asks for price and discount percentage.
Uses try/except to catch invalid inputs.
Prints the result or an error message.
"""

# function takes in price and percentage as arguments and returns the discounted price
def apply_discount(price, percentage):
    discount = price * percentage / 100
    return round(price - discount, 2)

# use the try block to catch invalid inputs
try:
    item_price = float(input("Enter item price: "))
    discount_percentage = float(input("Enter discount percentage: "))
    # final price is after applying the discount
    final_price = apply_discount(item_price, discount_percentage)
    discount_amount = round(item_price - final_price, 2)
    print(f"Original Price: {item_price} | Discount Amount: {discount_amount} | Final Price: {final_price}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    print("Discount percentage cannot be zero.")