# 🛠️ What you will create
# An anagram checker program that takes user input, validates it, and finds anagrams from a word list.

# Instructions:

# Download the provided text file (word list).
# Create anagram_checker.py with the AnagramChecker class.
# Create anagrams.py for the user interface.
# anagram_checker.py:



# Step 1: Create the AnagramChecker Class

# Create a class called AnagramChecker.
# Implement the __init__ method:
# Load the word list file into a variable (e.g., a set or list).
# Store the words in lowercase for case-insensitive comparison.


# Step 2: Implement is_valid_word Method

# Create a method called is_valid_word(word).
# Check if the given word exists in the loaded word list (case-insensitive).
# Return True if valid, False otherwise.


# Step 3: Implement is_anagram Method

# Create a method called is_anagram(word1, word2).
# Check if the sorted characters of word1 are equal to the sorted characters of word2.
# Return True if anagrams, False otherwise.


# Step 4: Implement get_anagrams Method

# Create a method called get_anagrams(word).
# Create an empty list to store anagrams.
# Iterate through the word list.
# For each word in the list, check if it’s an anagram of the given word using is_anagram.
# If it’s an anagram and not the same word, add it to the anagrams list.
# Return the list of anagrams.


# anagrams.py:

# Step 1: Import AnagramChecker

# Step 2: Create a Menu Loop

# Step 3: Get User Input and Validate

# Step 4: Find and Display Anagrams

# Create an instance of AnagramChecker.
# Use is_valid_word to check if the word is valid.
# Use get_anagrams to find anagrams.
# Display the word, its validity, and the anagrams in a formatted message.

########################################################################################################################################

from pathlib import Path


class AnagramChecker:
    def __init__(self, filename):
        file_path = Path(__file__).resolve().parent / filename
        with file_path.open('r', encoding='utf-8') as file:
            self.words = {word.strip().lower() for word in file if word.strip()}

    def is_valid_word(self, word):
        return word.strip().lower() in self.words

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def get_anagrams(self, word):
        target = word.strip().lower()
        return [w for w in sorted(self.words) if w != target and self.is_anagram(target, w)]
