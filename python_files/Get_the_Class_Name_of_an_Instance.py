# Program to get the class name of an instance

# Define a class
class MyClass:
    pass

# Create an instance of the class
obj = MyClass()

# Get the class name of the instance
class_name = obj.__class__.__name__

# Display the class name
print(f"The class name of the instance is: {class_name}")
