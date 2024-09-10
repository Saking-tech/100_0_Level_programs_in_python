# Program to differentiate between type() and isinstance()

# Define a class
class MyClass:
    pass

# Create an instance of the class
obj = MyClass()

# Use type() to check the object's class
print(f"type(obj): {type(obj)}")

# Use isinstance() to check if the object is an instance of MyClass
print(f"isinstance(obj, MyClass): {isinstance(obj, MyClass)}")
