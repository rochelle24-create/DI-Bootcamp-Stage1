# Daily Challenge: Coffee Shop Menu Manager
# You were hired to help a small coffee shop manage their product menu using Python.

# Write a program that:

# 1. Stores the coffee shop menu in memory
# 2. Lets the user:

# Create a new item
# Read (view) all items
# Update an item’s price
# Delete an item
# Exit
# Your program must be organized with functions.
# Do not write all the logic in one giant while loop.
# You should split behavior into reusable functions.



# 1. Data structure
# We will represent the menu using a dictionary called menu.

# The key is the drink name (string)
# The value is the price (float)
# Example starting data (you MUST start with this so tests are consistent):

# menu = {
#     "espresso": 7.0,
#     "latte": 12.0,
#     "cappuccino": 10.0
# }


# 2. Required functions
# You must implement the following functions.

# a) show_menu(menu_dict)
# Input: the dictionary
# Output: prints all items in the format drink - price₪
# If the menu is empty, print: "The menu is empty."
# Example:

# Current menu:
# espresso - 7.0₪
# latte - 12.0₪
# cappuccino - 10.0₪
# This function only prints. It does not return anything.



# b) add_item(menu_dict)
# Ask the user for:
# drink name
# price
# Add it to the dictionary.
# If the drink already exists, print "Item already exists!" and do not change the price.
# Example interaction:

# Enter new drink name: mocha
# Enter price: 14
# "mocha" added!
# This function mutates the dictionary. It does not return anything.



# c) update_price(menu_dict)
# Ask the user which drink they want to update.
# If it exists:
# ask for the new price
# update it
# print: "Price updated!"
# If it doesn’t exist:
# print: "Item not found."


# d) delete_item(menu_dict)
# Ask the user which drink to remove.
# If it exists:
# delete it from the dict
# print: "Item deleted."
# Otherwise:
# print: "Item not found."


# e) show_options()
# Prints the main menu of actions for the user:
# What would you like to do?
# 1. Show menu
# 2. Add item
# 3. Update price
# 4. Delete item
# 5. Exit
# Only prints. Doesn’t return anything.



# f) run_coffee_shop()
# This is the main controller of the program.

# Behavior:

# Keep running in a loop.
# Show options.
# Ask the user to choose (1-5).
# Depending on the choice, call the correct function.


# Rules:

# Invalid choice → print "Invalid choice, try again."
# Choice 5 stops the loop and prints "Goodbye!"


# 3. Program flow (example)
# This is what using the program might look like when it runs:

# What would you like to do?
# 1. Show menu
# 2. Add item
# 3. Update price
# 4. Delete item
# 5. Exit
# > 1
# Current menu:
# espresso - 7.0₪
# latte - 12.0₪
# cappuccino - 10.0₪

# What would you like to do?
# 1. Show menu
# 2. Add item
# 3. Update price
# 4. Delete item
# 5. Exit
# > 2
# Enter new drink name: mocha
# Enter price: 14
# "mocha" added!

# What would you like to do?
# 1. Show menu
# 2. Add item
# 3. Update price
# 4. Delete item
# 5. Exit
# > 3
# Which drink do you want to update? latte
# Enter the new price: 13
# Price updated!

# What would you like to do?
# 1. Show menu
# 2. Add item
# 3. Update price
# 4. Delete item
# 5. Exit
# > 4
# Which drink do you want to delete? espresso
# Item deleted!

# What would you like to do?
# 1. Show menu
# 2. Add item
# 3. Update price
# 4. Delete item
# 5. Exit
# > 1
# Current menu:
# latte - 13.0₪
# cappuccino - 10.0₪
# mocha - 14.0₪

# What would you like to do?
# 1. Show menu
# 2. Add item
# 3. Update price
# 4. Delete item
# 5. Exit
# > 5
# Goodbye!


# 4. Starter template (students fill in the TODOs)
# # Coffee Shop Menu Manager

# # Initial data
# menu = {
#     "espresso": 7.0,
#     "latte": 12.0,
#     "cappuccino": 10.0
# }

# def show_menu(menu_dict):
#     """Print all drinks and prices."""
#     pass



# def add_item(menu_dict):
#     """Add a new drink to the menu."""
#     pass


# def update_price(menu_dict):
#     """Change the price of an existing drink."""
#     pass


# def delete_item(menu_dict):
#     """Remove a drink from the menu."""
#     pass


# def show_options():
#     """Print the available actions."""
#     pass


# def run_coffee_shop():
#     """Main loop of the program."""
#     # TODO
#     # while True:
#     #   1. show_options()
#     #   2. get user choice
#     #   3. if 1 -> show_menu(menu)
#     #      if 2 -> add_item(menu)
#     #      if 3 -> update_price(menu)
#     #      if 4 -> delete_item(menu)
#     #      if 5 -> print("Goodbye!") and break
#     #      else -> "Invalid choice, try again."
#     pass


# # Start the program
# run_coffee_shop()

# Define the initial menu as a dictionary. Keys are drinks and Values are prices - shown as float.
menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}

def show_menu(menu_dict):
    if not menu_dict:
        print("The menu is empty.")
    else:
        print("Current menu:")
        for drink, price in menu_dict.items():
            print(f"{drink} - {price:.2f}₪")

def add_item(menu_dict):
    drink_name = input("Enter new drink name: ").lower()
    
    if drink_name in menu_dict:
        print("Item already exists!")
    else:
        price = float(input("Enter price: "))
        menu_dict[drink_name] = price
        print(f'"{drink_name}" added!')

def update_price(menu_dict):
    drink_name = input("Which drink do you want to update? ").lower()
    
    if drink_name in menu_dict:
        new_price = float(input("Enter the new price: "))
        menu_dict[drink_name] = new_price
        print("Price updated!")
    else:
        print("Item not found.")

def delete_item(menu_dict):
    drink_name = input("Which drink do you want to delete? ").lower()
    
    if drink_name in menu_dict:
        del menu_dict[drink_name]
        print("Item deleted.")
    else:
        print("Item not found.")

def show_options():
    print("What would you like to do?")
    print("1. Show menu")
    print("2. Add item")
    print("3. Update price")
    print("4. Delete item")
    print("5. Exit")

def run_coffee_shop():
    while True:
        show_options()
        choice = input("> ")
        
        if choice == "1":
            show_menu(menu)
        elif choice == "2":
            add_item(menu)
        elif choice == "3":
            update_price(menu)
        elif choice == "4":
            delete_item(menu)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
        print()

run_coffee_shop()

