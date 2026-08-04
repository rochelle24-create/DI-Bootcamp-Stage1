# 🌟 Exercise 1: Converting Lists into Dictionaries
# Key Python Topics:

# Creating dictionaries
# Zip function or dictionary comprehension


# Instructions
# You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.



# Lists:

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]


# Expected Output:

# # {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

my_dictionary=dict(zip(keys,values)) # dict zip appends items in lists into a dictionary.
print(my_dictionary.items())  


# 🌟 Exercise 2: Cinemax #2
# Key Python Topics:

# Looping through dictionaries
# Conditionals
# Calculations


# Instructions
# Write a program that calculates the total cost of movie tickets for a family based on their ages.

# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15


# Family Data:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.


# Bonus:

# Allow the user to input family members’ names and ages, then calculate the total ticket cost.


family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
sum = 0

for k, v in family.items():
    if v < 3:
        print(f"The price for {k} is free")
    if 3 < v < 12:
        print(f"The price for {k} is $10")
        sum += 10
    if v > 12:
        print(f"The price for {k} is $15")
        sum += 15
print(f"The total cost for your family is ${sum} ")

#Bonus 

your_family = {}

family_members = int(input("How many people in your family will be watching a movie today"))

for m in range(family_members):
    name = input("Enter a family member's name: ")
    age = input("Enter their age: ")
    your_family[name] = int(age)

print(your_family.items())   

sum = 0

for k, v in your_family.items():
    if v < 3:
        print(f"The price for {k} is free")
    if 3 < v < 12:
        print(f"The price for {k} is $10")
        sum += 10
    if v > 12:
        print(f"The price for {k} is $15")
        sum += 15
print(f"The total cost for your family is ${sum} ")



# 🌟 Exercise 3: Zara
# Key Python Topics:

# Creating dictionaries
# Accessing and modifying dictionary elements
# Dictionary methods like .pop() and .update()


# Instructions
# Create and manipulate a dictionary that contains information about the Zara brand.



# Brand Information:

# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green


# Create a dictionary called brand with the provided data. V
# Modify and access the dictionary as follows: 
# Change the value of number_stores to 2. V
# Print a sentence describing Zara’s clients using the type_of_clothes key. V
# Add a new key country_creation with the value Spain. V
# Check if international_competitors exists and, if so, add “Desigual” to the list. V
# Delete the creation_date key. V
# Print the last item in international_competitors. V
# Print the major colors in the US. V
# Print the number of keys in the dictionary. V
# Print all keys of the dictionary. V


# Bonus:

# Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.

brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': ['blue'],
        'Spain': ['red'],
        'US': ['pink', 'green']
    }
}


brand['number_stores']=2
print(brand.items()) 

print(f"Zara has {brand['type_of_clothes'][0:3]} clothing, so you will find something for every family member.")

brand.update(country_creation='Spain')

if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')

del brand['creation_date'] # Removes the creation_date Key and Value, removes the pair.
print(brand.items()) # Print the dictionary again without creation_date in the brand dictionary to check.

print(brand['major_color']['US'])

print(len(brand))
print(brand.keys())



# 🌟 Exercise 4: Disney Characters
# Key Python Topics:

# Looping with indexes
# Dictionary creation
# Sorting


# Instructions
# You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:



# Character List:

# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]


# Expected Results:

# 1. Create a dictionary that maps characters to their indices:

# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}


# 2. Create a dictionary that maps indices to characters:

# {0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}


# 3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:

# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

cartoon_char = ['Mickey', 'Minnie', 'Donald', 'Ariel', 'Pluto']

dict1 = {character: index for index, character in enumerate(cartoon_char)}
print("Dictionary 1 (Character -> Index):")
print(dict1)

dict2 = {index: character for index, character in enumerate(cartoon_char)}
print("\nDictionary 2 (Index -> Character):")
print(dict2)

sorted_characters = sorted(cartoon_char)                                            # sorted (Will sort alphabetically)
dict3 = {character: index for index, character in enumerate(sorted_characters)}
print("\nDictionary 3 (Sorted Character -> Index):")
print(dict3)
