# Program to calculate BMI

# Input weight (kg) and height (m)
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (cm): "))
height=100*height
# Calculate BMI
bmi = weight / (height ** 2)

# Display the BMI
print(f"Your BMI is {bmi:.2f}")
