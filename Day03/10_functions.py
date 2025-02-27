
"""  
Part 2: Functions

Why: Functions let you reuse logic—like a discount calculator you can call anywhere.

Learning Content
Define: def function_name(parameters):.
Return: Send a value back with return.

Example:
def add(a, b):
    return a + b
print(add(2, 3))  # 5

Task 2: Discount Function

Create discount_func.py in the same directory.

Write a program that:

Defines a function apply_discount(price, percentage) to calculate the discounted price.

Asks for price and discount percentage, calls the function, and prints the result.
"""


def apply_discount(price, percentage):
    discount = price * percentage / 100
    return price - discount


item_price = float(input("Enter item price: "))
discount_percentage = float(input("Enter discount percentage: "))

# call the function and store the result in a variable
final_price = apply_discount(item_price, discount_percentage)

discounted_price = round(item_price - discount_percentage, 2)

print(
    f"Original Price: {item_price} | Discount Amount: {discounted_price} | Final Price: {final_price}")

# print(
#     f"Original Price: {item_price} | Discount Amount: {discounted_price:2f} | Final Price: {final_price}")
