# Program to shuffle a deck of cards

import itertools, random

# Create a deck of cards
deck = list(itertools.product(['Spades', 'Hearts', 'Diamonds', 'Clubs'], 
                              ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']))

# Shuffle the deck
random.shuffle(deck)

# Display the shuffled deck
print("The shuffled deck of cards is:")
for card in deck:
    print(f"{card[1]} of {card[0]}")
