# Program to create a countdown timer

import time

# Input the number of seconds for the countdown
seconds = int(input("Enter the number of seconds: "))

# Countdown loop
while seconds > 0:
    print(f"Time left: {seconds} seconds")
    time.sleep(1)
    seconds -= 1

# Display message when the countdown ends
print("Time's up!")
