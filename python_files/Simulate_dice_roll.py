# Program to simulate a dice roll

import random

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Roll the dice
print(f"You rolled a {roll_dice()}")
