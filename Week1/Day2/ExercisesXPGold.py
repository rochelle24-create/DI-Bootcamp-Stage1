# What we will learn:
# Python Basics
# Python data types
# Loops


# Exercise 1: Concatenate lists
# Instructions
# Write code that concatenates two lists together without using the + sign.

list_a = [1,2,3,4,5]    # create list A
list_b = [6,7,8,9,10]   # create list B

list_a.extend(list_b)   # Joined the two lists using extend.
print(list_a)           # Print to show new list A which has changed 



# Exercise 2: Range of numbers
# Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
multiples = []                                                                      # Define a new blank list called "multiples" that will include all numbers divisible by 5 and 7.
for n in range(1500,2501):                                                          # Define the range of numbers to iterate through from 1500 up to 2500 including the last number in our range (range 2500+1)
            if n % 5 ==0 and n % 7 ==0:                                             # Check if divisible by 5 and 7 without a remainder.
                    multiples.append(n)                                             # Append number to list "multiples".
print(multiples)                                                                    # Print our list to show the multiples of 5 and 7.
                    



# Exercise 3: Check the index
# Instructions
# Using this variable

# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.

# Example: if input is 'Cortana' we should be printing the index 1


# Exercise 4: Greatest Number
# Instructions
# Ask the user for 3 numbers and print the greatest number.

# Test Data
# Input the 1st number: 25
# Input the 2nd number: 78
# Input the 3rd number: 87

# The greatest number is: 87


# Exercise 5: The Alphabet
# Instructions
# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.


# Exercise 6: Words and letters
# Instructions
# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable called letter.
# Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
# If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.


# Exercise 7: Min, Max, Sum
# Instructions
# Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. Use the sum() function to see how quickly Python can add a million numbers.



# Exercise 8 : List and Tuple
# Instructions
# Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.

# Suppose the following input is supplied to the program: 34,67,55,33,12,98

# Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')


# Exercise 9 : Random number
# Instructions
# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says Winner.
# If the user guesses the wrong number print a message that says better luck next time.
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop tally up and display total games won and lost.