# What You Will Create:

# A Rock Paper Scissors game where the user plays against the computer, with a menu, game logic, and score tracking.



# Instructions:

# Create a directory for the game.
# Create rock-paper-scissors.py (for menu, input, and summary).
# Create game.py (for game logic).


# Part I - game.py

# Step 1: Create the Game Class



# Step 2: Implement get_user_item Method

# Create a method called get_user_item(self).
# Ask the user to select an item (rock/paper/scissors).


# Step 3: Implement get_computer_item Method

# Create a method called get_computer_item(self).
# Randomly select an item (rock/paper/scissors).
# Return the computer’s item.


# Step 4: Implement get_game_result Method

# Create a method called get_game_result(self, user_item, computer_item).
# Take user_item and computer_item as parameters.
# Determine the result of the game based on the rules of Rock Paper Scissors.
# Return “win”, “draw”, or “loss”.


# Step 5: Implement play Method

# Create a method called play(self).
# Call get_user_item() to get the user’s choice.
# Call get_computer_item() to get the computer’s choice.
# Call get_game_result() to determine the result.
# Print the outcome of the game (user’s choice, computer’s choice, result).
# Return the result (“win”, “draw”, or “loss”) as a string.


# Example (Conceptual, No Direct Solution):

# import random

# class Game:
#     def get_user_item(self):
#         # ... code to get and validate user input ...
#         # ... code to return user's choice ...

#     def get_computer_item(self):
#         # ... code to generate computer's choice ...
#         # ... code to return computer's choice ...

#     def get_game_result(self, user_item, computer_item):
#         # ... code to determine and return game result ...

#     def play(self):
#         # ... code to get user and computer choices ...
#         # ... code to determine game result ...
#         # ... code to print game outcome ...
#         # ... code to return game result ...


# Part II - rock-paper-scissors.py

# Step 6: Implement get_user_menu_choice Function

# Create a function called get_user_menu_choice().
# Display the menu options (“Play a new game”, “Show scores”, “Quit”).
# Get the user’s choice.
# Validate the input (e.g., check if it’s one of the valid options).
# Return the user’s choice.


# Step 7: Implement print_results Function

# Create a function called print_results(results).
# Take a dictionary called results as a parameter (e.g., {"win": 2, "loss": 4, "draw": 3}).
# Print the results in a user-friendly format (e.g., “Wins: 2, Losses: 4, Draws: 3”).
# Thank the user for playing.


# Step 8: Implement main Function

# Create a function called main().
# Pepeatedly show the menu until the user chooses to exit.
# Call get_user_menu_choice() to get the user’s choice.
# If the user chooses to play a game:
# Create a Game object.
# Call the play() method of the Game object.
# Store the result of the game in a dictionary (e.g., results).
# If the user chooses to exit:
# Call print_results() to display the game summary.
# Exit the program.

######################################################################################################################################


import random

class Game:
    def __init__(self):
        self.items = ["Rock", "Paper", "Scissors"]
        self.user_item = None
        self.computer_item = None

def get_user_item(self):
    while True:
        user_input = input("Enter your choice, Rock, Paper or Scissors here: ")
        user_input = user_input.capitalize()
    
        if user_input in self.items:
            self.user_item = user_input
            return user_input
        else:
            print("Invalid choice! Please try again.")

def get_computer_item(self):
    self.computer_item = random.choice(self.items)
    return self.computer_item
       
def get_game_result(self, user_item, computer_item):
    if user_item == computer_item:
        return "draw"
    
    if user_item == "Rock" and computer_item == "Scissors":
        return "win"
    elif user_item == "Paper" and computer_item == "Rock":
        return "win"
    elif user_item == "Scissors" and computer_item == "Paper":
        return "win"
    
    else:
        return "loss"
def play(self):
    self.get_user_item()
    self.get_computer_item()
    result = self.get_game_result(self.user_item, self.computer_item)
    
    print(f"Your choice: {self.user_item}")
    print(f"Computer's choice: {self.computer_item}")
    print(f"Result: {result}")
    
    return result