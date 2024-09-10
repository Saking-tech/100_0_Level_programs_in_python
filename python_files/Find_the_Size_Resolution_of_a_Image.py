# Program to find the size (resolution) of an image

from PIL import Image

# Input the image file path
image_path = input("Enter the image file path: ")

# Open the image
with Image.open(image_path) as img:
    # Get the width and height
    width, height = img.size

# Display the resolution
print(f"Resolution of the image is {width}x{height}")
