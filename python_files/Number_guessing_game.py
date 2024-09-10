# Program for number guessing game

import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Start the game
while True:
    guess = int(input("Guess the number (between 1 and 100): "))
    
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number!")
        break
