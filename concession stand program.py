# Concession Stand Program


# We are creating a menu of item what we have.
menu = {"Pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

# we will create empty cart for customer to picup items and also a total for it.
cart = []
total = 0

# we are iterating throw a menu.
print("_________MENU________")
for key, value in menu.items():
    print(f"{key:9}: ${value:.2f}")
print("________________________")


# we will do while loop throw customer input and on the menu selection on cart or quit the menu.
while True:
    food = input("Select an item (q to Quit):  ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

# let's calculate a total bill.
print("_________YOUR ORDER________")
for food in cart:
    total += menu.get(food)
    print(f"{food},", end=" ")

print(f"Total bill is: ${total:.2f}")
