# Program to simulate a biased dice roll

import random

# Define a function for biased dice roll
# The probability of rolling 6 is higher than other numbers
def biased_dice():
    probabilities = [1, 2, 3, 4, 5, 6, 6, 6, 6, 6]  # Giving higher weight to 6
    return random.choice(probabilities)

# Roll the biased dice
for i in range(10):  # Simulate 10 rolls
    print(f"Roll {i+1}: {biased_dice()}")
