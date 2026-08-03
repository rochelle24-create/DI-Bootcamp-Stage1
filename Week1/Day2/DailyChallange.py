# Challenge 1: Multiples of a Number


# Key Python Topics:
# input() function
# Loops (for or while)
# Lists and appending items
# Basic arithmetic (multiplication)


# Instructions:
# 1. Ask the user for two inputs:

# A number (integer).
# A length (integer).
# 2. Create a program that generates a list of multiples of the given number.
# 3. The list should stop when it reaches the length specified by the user.

number = int(input("Enter a number: "))                         # Get user input for number to multiply.
the_length = int(input("Enter the length of the list: "))       # Get user input for length of multiplication list.
multiplication_list = []                                        # Define a list called multiplication list that we are creating.
for m in range(1,the_length+1):                                 # Multiply the user's number for the length of times from user's input. (Starting with 1 and not 0,len+1) to get the correct range for length.
         multiplication_list.append(m*number)                   # Building the multiplication list.
print(multiplication_list)                                      #printing the output to show the new multiplication list.





# Example 1:

# Input:

# number: 7
# length: 5
# Output:
# [7, 14, 21, 28, 35]



# Example 2:

# Input:

# number: 12
# length: 10
# Output:
# [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]



# Example 3:

# Input:

# number: 17
# length: 6
# Output:
# [17, 34, 51, 68, 85, 102]



# Challenge 2: Remove Consecutive Duplicate Letters


# Key Python Topics:
# input() function
# Strings and string manipulation
# Loops (for or while)
# Conditional statements (if)


# Instructions:
# 1. Ask the user for a string.
# 2. Write a program that processes the string to remove consecutive duplicate letters.

# The new string should only contain unique consecutive letters.
# For example, “ppoeemm” should become “poem” (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
# 3. The program should print the modified string.



# Example 1:

# Input:
# user’s word: "ppoeemm"
# Output:
# "poem"


# Example 2:

# Input:
# user’s word: "wiiiinnnnd"
# Output:
# "wind"


# Example 3:

# Input:
# user’s word: "ttiiitllleeee"
# Output:
# "title"


# Example 4:

# Input:
# user’s word: "cccccaaarrrbbonnnnn"
# Output:
# "carbon"


# Notes:
# The final string will not include any consecutive duplicates, but non-consecutive duplicates are allowed.
# Example: In "recursive", the two ‘r’s and two ‘e’s are allowed because they are not consecutive.

funny_string = input("Type a funny string with consecutive duplicate letters: ") # Get string from user.
fixed_string = funny_string[0]                                                   # Define new list starting with the first letter in the string.

for i in range(1, len(funny_string)):                                            # Check for consecutive duplicate letters starting from the second letter, note that range begins at (index 1).
    if funny_string[i] != funny_string[i-1]:                                     # Build fixed string without any consecutive duplicate letters
        fixed_string += funny_string[i]                                          # Build fixed string without any consecutive duplicate letters
        
print(str(fixed_string))                                                         # Prints new string without consecutive duplicates.


          




