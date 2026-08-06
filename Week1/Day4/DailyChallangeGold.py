# Goal: Decrypt a hidden message from a matrix string by processing it column-wise and filtering characters.



# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# Python Basics
# Conditionals
# Loops
# Functions
# Lists (2D lists/matrices)
# String Manipulation


# Key Python Topics:

# Strings
# Lists (2D lists)
# Loops (for loops)
# Conditional statements (if, else)
# String methods (.isalpha(), etc.)
# String concatenation.


# Instructions:

# You are given a “Matrix” string:



# MATRIX_STR = '''
# 7ir
# Tsi
# h%x
# i ?
# sM# 
# $a 
# #t%'''       


# This represents a grid of characters, and your task is to decode the hidden message within.



# Understanding the Matrix:

# Imagine this string arranged in rows and columns, forming a grid.
# To work with it in Python, you’ll need to transform this string into a 2D list (a list of lists), where each inner list represents a row.


# Step 1: Transforming the String into a 2D List



# Step 2: Processing Columns

# Neo reads the matrix column by column, from top to bottom, starting from the leftmost column.
# You’ll need to write code that iterates through the columns of your 2D list.
# Think about how you can access the elements of a 2D list by column.


# Step 3: Filtering Alpha Characters

# only select alpha characters (letters).
# For each character in a column, check if it’s an alpha character.
# If it is, add it to a temporary string.
# Think about how you can check if a character is an alphabet letter.


# Step 4: Replacing Symbols with Spaces

# Replace every group of symbols (non-alpha characters) between two alpha characters with a space.
# After you have gathered the alpha characters, you will need to iterate through them, and where there are non alpha characters between them, you will insert a space.
# Think about how you can keep track of when you encounter an alphabet character, and when you encounter a non alphabet character.


# Step 5: Constructing the Secret Message

# Combine the filtered and processed characters to form the decoded message.
# Print the decoded message.


# Example:


# # Step 1: Convert matrix_string to a 2D list (matrix)
# matrix = []
# # ... code to create matrix ...

# # Step 2: Iterate through columns
# # ... code to iterate through columns ...

# # Step 3: Filter alpha characters
# # ... code to filter alpha characters ...

# # Step 4: Replace symbols with spaces
# decoded_message = ""
# # ... code to replace symbols with spaces ...

# # Step 5: Print the decoded message
# print(decoded_message)

MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%''' 

rows = MATRIX_STR.strip().split('\n')
matrix = [list(row) for row in rows]

secret_message = ""
num_column = len(matrix[0])

for column in range(num_column):
    column_chars = [matrix[row][column] for row in range(len(matrix)) if column < len(matrix[row])]
    for char in column_chars:
        if char.isalpha():
            secret_message += char
        else:
            secret_message += ' '
print(f"THIS IS THE SECRET MESSAGE: {secret_message}")