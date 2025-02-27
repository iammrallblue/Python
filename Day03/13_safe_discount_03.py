

"""  
4. Raising Exceptions
Now: You catch errors from float().
Next Level: Create your own rules.
Example:
python
try:
    item_price = float(input("Enter item price: "))
    if item_price < 0:
        raise ValueError("Price cannot be negative!")
    discount_percentage = float(input("Enter discount percentage: "))
    final_price = apply_discount(item_price, discount_percentage)
    discount_amount = round(item_price - final_price, 2)
    print(f"Original Price: {item_price} | Discount Amount: {discount_amount} | Final Price: {final_price}")
except ValueError as e:
    print(f"Error: {e}")
Why: Enforces business logic (e.g., no negative prices).
"""