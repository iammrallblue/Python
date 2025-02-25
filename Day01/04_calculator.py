
""" 
Simple Shopping Calculator

Write a program that:
    Asks for an item name.
    Asks for its price.
    Asks for quantity.
    Calculates the total.
    If total > 50, applies a 10% discount.
    Prints the final price.

Q: Why do we need float() or int() for price and quantity? A: input() returns strings, so we need to convert them to numbers.

Q: What happens if you remove int() and type 3.5 for quantity? A: It crashes because you can’t multiply a string by a float.

Q: Why does if total > 50 only run sometimes? A: It checks the condition and only applies the discount if TRUE.

Q: How does total = total * 0.9 change the value? A: It multiplies total by 0.9 (or 90%) and stores the result back in total. 
"""

item = input("Enter item name: ")
price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
total = price * quantity

if total > 50:
    print('You spent more than 50, applying "10%" discount.')
    total = total * 0.9
print("Item: ", item, "Final price is:", total)


