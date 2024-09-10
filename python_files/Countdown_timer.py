# Program to create a countdown timer

import time

# Input the countdown time in seconds
seconds = int(input("Enter time in seconds: "))

# Countdown loop
while seconds:
    mins, secs = divmod(seconds, 60)
    timer = f'{mins:02d}:{secs:02d}'
    print(timer, end="\r")
    time.sleep(1)
    seconds -= 1

# Display time's up message
print("Time's up!")
