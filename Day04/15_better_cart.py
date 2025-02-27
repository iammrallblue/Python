
"""  
Why: Lists are your cart’s foundation, but let’s make it more practical—add prices, validation, and a total cost, mimicking a real shop cart.

Key Knowledge Points
Lists as Dynamic Storage:
Lists grow with append(), shrink with remove()—great for carts where items change.

Why: In Django, lists might hold temporary data before saving to a database.

Indexing: 
cart[0] accesses the first item—useful for item details.

Why: You’ll use this to display or edit specific cart items.

Iteration:
for item in cart: loops through items—key for summarizing carts.

Why: Lists items on a webpage.

Limitations:
Lists alone don’t persist (gone when the program ends)—later, Django’s database will fix this.

No key-value pairing (e.g., name:price)—dictionaries will help soon.


Task: Enhanced Shopping Cart

Write a program that:

Starts with an empty cart.

Asks for 3 items (name and price).

Stores each as a mini-list [name, price].

Prints the cart and calculates the total cost.
"""

better_cart = []  # List of [name, price] mini-lists/sublists

# Q: What is a mini-list? A: It is a list within a list, used to store related data together.

# Q: what is range() used for? A: It is a built-in function that generates a sequence of numbers.

for i in range(3):
    item_name = input(f"Add item {i + 1} name: ")
    while True:  # validate price
        # this try...except block ensures that the price is a number
        try:
            item_price = float(input(f"Add item {i + 1} price: "))
            # if condition ensures that the price is positive
            if item_price < 0:
                print("Price must be positive.")
                continue
            break
        except ValueError:
            print("Price must be a number. Try again.")
    # add the item to the cart after validation
    better_cart.append([item_name, item_price])


# print("Your Cart:", better_cart)
# Your Cart: [['S Condom', 6.99], ['M Condom', 7.99], ['L Condom', 9.99]]

# calculate the total cost
total_cost = 0
# print("Your Cart:")
# for item in better_cart:
#     print(f"{item[0]}: ${item[1]}")
#     total_cost += item[1]

# print(f"Total cost: ${total_cost}")


"""  
Why Used Here: 

In better_cart.py, enumerate(better_cart) gives you i (the position) and item (the sublist [name, price]). We use i + 1 to number items starting from 1 instead of 0, making it user-friendly (e.g., “1: S Condom” vs. “0: S Condom”).

Alternative: Without enumerate(), you could use range(len(better_cart)):
python

for i in range(len(better_cart)):
    print(f"{i+1}: {better_cart[i][0]}: ${better_cart[i][1]}")

But enumerate() is cleaner and more Pythonic (idiomatic).

E-commerce Relevance: When displaying a cart on a website, you’ll often number items (e.g., “1. S Condom - $6.99”)—enumerate() simplifies this.
"""

print("Shopping Cart:")
for i, item in enumerate(better_cart):
    print(f"{i + 1}: {item[0]}: ${item[1]}")
    total_cost += item[1]

print(f"Total cost: ${round(total_cost,2)}")
