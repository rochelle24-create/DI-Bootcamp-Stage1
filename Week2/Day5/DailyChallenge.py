# Instructions:



# Exercise 1: Quizz
# Answer the following questions:

Questions:
#1 What is a class?
#2 What is an instance?
#3 What is encapsulation?
#4 What is abstraction?
#5 What is inheritance?
#6 What is multiple inheritance?
#7 What is polymorphism?
#8 What is method resolution order or MRO?

Answers:
# 1. A class is a template for an object with structure and differnet behaiviors and attributes.
# 2. An instance is an object from the class created from the template.
# 3. Encapsulatioin is the idea of bundling and hiding the internal details of attributes and methods.
# 4. Abstraction is the idea of the user only interacting with the outmost layer of what something does without knowing it's inner workings.
# 5. Inheritence is the ability of a class to pass down or to aquire attributes from a parent class or to a child class, it gets the existing attribues and methods.
# 6. Multiple Inheritance means a class inherits from more than one parent class. It gets attributes and methods from all of them.
# 7. Polymorphism means many faces, it is a concept that means that different methods can take on different forms depending on the type of object.
# 8. MRO is the order of the inheritence of a method that might inheret from more than one class, with MRO the first class in the order matters.

##########################################################################################################################################################################

# Exercise 2: Create a deck of cards class
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.

import random


class Card:
    
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    def __init__(self, suit, value):
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit: {suit}. Must be one of {self.SUITS}")
        if value not in self.VALUES:
            raise ValueError(f"Invalid value: {value}. Must be one of {self.VALUES}")
        
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    
    def __init__(self):
        self.cards = []
        self.shuffle()
    
    def shuffle(self):
        self.cards = []
        for suit in Card.SUITS:
            for value in Card.VALUES:
                self.cards.append(Card(suit, value))
        
        random.shuffle(self.cards)
    
    def deal(self):
        if len(self.cards) == 0:
            raise IndexError("Cannot deal from an empty deck")
        
        return self.cards.pop()
    
    def __repr__(self):
        return f"Deck with {len(self.cards)} cards remaining"


if __name__ == "__main__":
    deck = Deck()
    print(f"Created: {deck}")
    print(f"Total cards: {len(deck.cards)}\n")
    
    print("Dealing 5 cards:")
    for i in range(5):
        card = deck.deal()
        print(f"  {i+1}. {card}")
    
    print(f"\n{deck}")
    print(f"Cards remaining: {len(deck.cards)}\n")
    
    print("Shuffling the deck...")
    deck.shuffle()
    print(f"{deck}")
    print(f"Cards remaining: {len(deck.cards)}\n")
    
    print("Dealing all remaining cards...")
    count = 0
    while len(deck.cards) > 0:
        deck.deal()
        count += 1
    print(f"Successfully dealt {count} cards")
    print(f"{deck}")