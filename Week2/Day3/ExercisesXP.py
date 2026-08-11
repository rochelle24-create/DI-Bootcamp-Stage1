# Exercise 1: Currencies
# Goal: Implement dunder methods for a Currency class to handle string representation, integer conversion, addition, and in-place addition.



# Key Python Topics:

# Dunder methods (__str__, __repr__, __int__, __add__, __iadd__)
# Type checking (isinstance())
# Raising exceptions (raise TypeError)


# Instructions:

# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount

#     #Your code starts HERE


# Using the code above, implement the relevant methods and dunder methods which will output the results below.

# Hint : When adding 2 currencies which don’t share the same label you should raise an error.

# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 1)
# c4 = Currency('shekel', 10)

# #the comment is the expected output
# print(c1)
# # '5 dollars'

# print(int(c1))
# # 5

# print(repr(c1))
# # '5 dollars'

# print(c1 + 5)
# # 10

# print(c1 + c2)
# # 15

# print(c1) 
# # 5 dollars

# c1 += 5
# print(c1)
# # 10 dollars

# c1 += c2
# print(c1)
# # 20 dollars

# print(c1 + c3)
# # TypeError: Cannot add between Currency type <dollar> and <shekel>
# #comment the print above before you run the file for next exercises (since the error will crash your file)


# 🌟 Exercise 2: Import
# Goal: Create a module with a function and import it into another file.



# Instructions:

# Create a func.py file with a function that sums two numbers and prints the result. Then, import and call the function from exercise_one.py.



# Key Python Topics:

# Modules (creating and importing)
# Functions


# Step 1: Create func.py

# Create a file named func.py.
# Define a function inside that file that takes two numbers as arguments, sums them, and prints the result.


# Step 2: Create exercise_one.py

# Create a file named exercise_one.py.
# Import the function from func.py using one of the import syntaxes provided in the instructions.
# Call the imported function with two numbers.


# 🌟 Exercise 3: String module
# Goal: Generate a random string of length 5 using the string module.



# Instructions:

# Use the string module to generate a random string of length 5, consisting of uppercase and lowercase letters only.



# Key Python Topics:

# string module
# random module
# String concatenation


# Step 1: Import the string and random modules

# Import the string and random modules.


# Step 2: Create a string of all letters

# Read about the strings methods HERE to find the best methods for this step



# Step 3: Generate a random string

# Use a loop to select 5 random characters from the combined string.
# Concatenate the characters to form the random string.


# 🌟 Exercise 4: Current Date
# Goal: Create a function that displays the current date.



# Key Python Topics:

# datetime module


# Instructions:

# Use the datetime module to create a function that displays the current date.

# Step 1: Import the datetime module

# Step 2: Get the current date

# Step 3: Display the date



# 🌟 Exercise 5: Amount of time left until January 1st
# Goal: Create a function that displays the amount of time left until January 1st.



# Key Python Topics:

# datetime module
# Time difference calculations


# Instructions:

# Use the datetime module to calculate and display the time left until January 1st.
# more info about this module HERE

# Step 1: Import the datetime module

# Step 2: Get the current date and time

# Step 3: Create a datetime object for January 1st of the next year

# Step 4: Calculate the time difference

# Step 5: Display the time difference



# 🌟 Exercise 6: Birthday and minutes
# Key Python Topics:

# datetime module
# datetime.datetime.strptime() (parsing dates)
# Time difference calculations
# .total_seconds() method


# Instructions:

# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.



# 🌟 Exercise 7: Faker Module
# Goal: Use the faker module to generate fake user data and store it in a list of dictionaries.
# Read more about this module HERE



# Key Python Topics:

# faker module
# Dictionaries
# Lists
# Loops


# Instructions:

# Install the faker module and use it to create a list of dictionaries, where each dictionary represents a user with fake data.

# Step 1: Install the faker module

# Step 2: Import the faker module

# Step 3: Create an empty list of users

# Step 4: Create a function to add users

# Create a function that takes the number of users to generate as an argument.
# Inside the function, use a loop to generate the specified number of users.
# For each user, create a dictionary with the keys name, address, and language_code.
# Use the faker instance to generate fake data for each key:
# name: faker.name()
# address: faker.address()
# language_code: faker.language_code()
# Append the user dictionary to the users list.
# Step 5: Call the function and print the users list

#######################################################################################################################################

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}s"
    
    def __repr__(self):
        return f"{self.amount} {self.currency}s"
    
    def __int__(self):
        return self.amount
    
    def __add__(self, other):
        if isinstance(other, int):
            return self.amount + other
        
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
    
    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        return self

############################################################################################################################
#Exercise 2: Import

#In files:

#*** file name exercise_one.py ***

from func import sum_numbers

sum_numbers(8, 6)
sum_numbers(20, 30)
#______________________________________________

#*** file name func.py ***

def sum_numbers(a,b):
    result = int(a)+int(b)
    print(f"The sum of these two numbers {a} and {b} is: {result}.")
#################################################################################################################################
# Exercise 3: String module

import string
import random

letters = string.ascii_letters

random_string = ""
for i in range(5):
    random_string += random.choice(letters)

print(random_string)

#################################################################################################################################
# Exercise 4: Current Date

from datetime import datetime

def show_current_date():
    current_date = datetime.now()
    print(current_date)

show_current_date()

#################################################################################################################

# Exercise 5: Amount of time left until January 1st
# Goal: Create a function that displays the amount of time left until January 1st

from datetime import datetime

from datetime import datetime

def time_until_jan_1st():
    time_now = datetime.now()
    next_year = time_now.year + 1
    jan_1st = datetime(next_year, 1, 1)
    time_left = jan_1st - time_now

    print(time_left)

time_until_jan_1st()

#################################################################################################################################
#  Exercise 6: Birthday and minutes

from datetime import datetime

def minutes_lived(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")
    now = datetime.now()
    time_lived = now - birthdate
    minutes = time_lived.total_seconds() / 60

    print(f"You have lived {int(minutes)} minutes!")

minutes_lived("07/03/2005")
minutes_lived("07/07/1988") #Checking my birthday ;)

################################################################################################################################
# Exercise 7: Faker Module

# Installation of Faker Module
# #PS C:\Users\roche> pip install faker
# Collecting faker
#   Downloading faker-40.36.0-py3-none-any.whl.metadata (16 kB)
# Requirement already satisfied: tzdata in .\AppData\Local\Programs\Python\Python314\Lib\site-packages (from faker) (2025.3)
# Downloading faker-40.36.0-py3-none-any.whl (2.1 MB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 9.9 MB/s  0:00:00
# #Installing collected packages: faker

from faker import Faker

fake = Faker()
users = []

def add_users(n):
    for i in range(n):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
        users.append(user)

add_users(5)
print(users)