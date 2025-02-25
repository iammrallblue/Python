
'''
User input for item name and price

Input/Output: Getting data from users and showing results.
'''
item = input("Enter item name: ")
price = float(input("Enter item price: "))
print("You bought", item, "for", price)

""" 
input("Enter item price: "): Asks for a number, returns it as a string (e.g., "120").
float(...): Turns the string into a number (e.g., 120.0).
"""


print()
print()


'''
Discount for expensive items

Conditionals: Making decisions based on conditions.
'''
price = float(input("Enter item price: "))
if price > 100:
    print("Too expensive! Applying 20% discount.")
    price = price * 0.8
print("Final price is:", price)

'''
if price > 100:: Checks if the number exceeds 100.

price = price * 0.8: If true, multiplies by 0.8 (20% off).
print(...): Shows the final result, discounted or not.
'''
