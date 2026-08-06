
# What you will learn
# Conditionals
# Loops
# Functions
# Modules


# What you will create
# Use python to create a Hangman game.



# Instructions
# The computer choose a random word and mark stars for each letter of each word.
# Then the player will guess a letter.
# If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
# If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
# The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
# The player can’t guess the same letter twice.


# Starter code
# Here is a piece of code that will give you a random word.

#     import random

#     wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
#     word = random.choice(wordslist) 

    ### YOUR CODE STARTS FROM HERE ###

import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)
print(word) # Printing word for testing


wrong_guess = 0 
alphabet = set()
characters = {letter: False for letter in word}
body_parts = ['head', 'body', 'left_arm', 'right_arm','left_leg','right leg']

while wrong_guess < 6:
    player_guess = input("Guess a letter: ")
    if player_guess in alphabet:
        print(f"You already guessed {player_guess}! Try a different letter.")
        continue
    alphabet.add(player_guess)
    
    if player_guess in word:
        print(f"Great guess, the letter {player_guess} is in the word.")
        characters[player_guess] = True
    else:
        print(f"Wrong! {player_guess} is not in the word.")
        wrong_guess += 1
    
    if wrong_guess > 0:
        displayed_parts = body_parts[:wrong_guess]
        print(f"Wrong guesses: {wrong_guess}")
        print(f"Body parts shown: {', '.join(displayed_parts)}")
    
    word_build = "".join([letter if characters[letter] else "_" for letter in word])
    print(word_build)
    
    if word_build == word:
        print("You won!")
        break

if word_build == word:
    print("Game Over! You won!")
else:
    print(f"Game Over! You lost! The word was: {word}")

                      

