# 🌟 Exercise 1: Favorite Numbers
# Key Python Topics:

# Sets
# Adding/removing items in a set
# Set concatenation (using union)


# Instructions:

# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.

my_fav_numbers = {7,8,2,4,6,8,10,18,20}
#print(type(my_fav_numbers)) # Checking the type of my_fav_numbers / it is supposed to be a set.
my_fav_numbers.add(30)
my_fav_numbers.add(40)
print(my_fav_numbers)

friend_fav_numbers = {100,200,300,400,500}
#print(type(friend_fav_numbers)) # Checking the type of friend_fav_numbers / it is supposed to be a set.
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)


# 🌟 Exercise 2: Tuple
# Key Python Topics:

# Tuples (immutability)


# Instructions:

# Given a tuple of integers, try to add more integers to the tuple.
# Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.

my_tuple = (1,2,3,4,5)
your_tuple = (10,20,30,40,50)
print(type(my_tuple))
print(type(your_tuple))
#my_tuple.append(your_tuple) # We get AttributeError: 'tuple' object has no attribute 'append'
#my_tuple[4] = 40 # We get TypeError: 'tuple' object does not support item assignment




# 🌟 Exercise 3: List Manipulation
# Key Python Topics:

# Lists
# List methods: append, remove, insert, count, clear


# Instructions:

# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples") # Inserts Apples to index 0 to be at the begining of the list, not append which is at the end of the list.
basket.count("Apples")
print(basket.count("Apples"))
basket.clear()
print(basket)


# 🌟 Exercise 4: Floats
# Key Python Topics:

# Lists
# Floats and integers
# Range generation


# Instructions:

# Recap: What is a float? What’s the difference between a float and an integer?
# Create a list containing the following sequence of mixed types: floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?

my_list = []
for n in range(3, 11):
            my_list.append(n/2)
print(my_list)



# 🌟 Exercise 5: For Loop
# Key Python Topics:

# Loops (for)
# Range and indexing


# Instructions:

# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.

for n in range(1, 21):
    print(n)

even_index_numbers = list(range(1, 21))
for i in range(0, len(even_index_numbers), 2):
    print(even_index_numbers[i])

# 🌟 Exercise 6: While Loop
# Key Python Topics:

# Loops (while)
# Conditionals


# Instructions:

# Use an input to ask the user to enter their name.
# Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# hint: check for the method isdigit()
# if the input is incorrect, keep asking for the correct input until it is correct
# if the input is correct print “thank you” and break the loop
# Example:

# Alt text

while True:
    name = input("Enter your name: ")
    
    if name.isdigit() or len(name) < 3:
        print("Name must be at least 3 letters and you cant use any numbers.")
        continue

    print("Thank you!")
    break



# 🌟 Exercise 7: Favorite Fruits
# Key Python Topics:

# Input/output
# Strings and lists
# Conditionals


# Instructions:

# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"

fruits_list = []
favorite_fruits=input("List some of your favorite fruits separated by a ' ' space and press Enter: ")
fruits_list = favorite_fruits.split()
choice=input("Choose a fruit to eat today, type here: ")
if choice in fruits_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")
                


     
# 🌟 Exercise 8: Pizza Toppings
# Key Python Topics:

# Loops
# Lists
# String formatting


# Instructions:

# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.

total_toppings = []
while True:
    toppings=input("Let's build your piza, list your topping and press Enter. Type 'end' to exit.:  ")
    if toppings== 'end':
        break          
    total_toppings.append(toppings)
    print(f"Great, adding {toppings} to your pizza")

pizza_price = 10 + (len(total_toppings) * 2.5)
#print(type(pizza_price))                                       # Checking, price should be a float.

print(total_toppings)
print(f"The price of your pizza today will be {pizza_price}$")

# 🌟 Exercise 9: Cinemax Tickets
# Key Python Topics:

# Conditionals
# Lists
# Loops


# Instructions:

# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.

total_cost = 0
family_members = []

while True:
    age_input = input("Enter the age of a family member (or 'done' to finish): ")
    
    if age_input.lower() == 'done':
        break
    
    age = int(age_input)
    family_members.append(age)
    
    if age < 3:
        cost = 0
        print(f"Age {age}: Free ticket")
    elif age <= 12:
        cost = 10
        print(f"Age {age}: $10 ticket")
    else:
        cost = 15
        print(f"Age {age}: $15 ticket")
    
    total_cost += cost

print(f"\nFamily members' ages: {family_members}")
print(f"Total ticket cost: ${total_cost}")

# Bonus:

# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
# Print the final list of attendees.

pproved_customers = []
while True:
    customer_age = input("What is this person's age? Type 'end' to exit: ")
    if customer_age == 'end':
        break
    customer_age = int(customer_age)
    if 16 <= customer_age <= 21:
        approved_customers.append(customer_age)
    else:
        print("You cannot view this movie")

print(f"Final list: {approved_customers}")

