# Program to measure the elapsed time in Python

import time

# Start the timer
start_time = time.time()

# Perform some task (e.g., a loop)
for i in range(1000000):
    pass

# Stop the timer
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Display the elapsed time
print(f"Elapsed time: {elapsed_time} seconds")
