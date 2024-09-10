# Program to represent enum

from enum import Enum

# Define an enumeration for colors
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Access enum members
print(f"Color.RED: {Color.RED}")
print(f"Color.GREEN: {Color.GREEN}")
print(f"Color.BLUE: {Color.BLUE}")

# Access enum values
print(f"Value of Color.RED: {Color.RED.value}")
