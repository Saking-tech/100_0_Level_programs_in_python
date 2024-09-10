# Program for temperature conversion

# Input temperature and conversion choice
temp = float(input("Enter temperature: "))
choice = input("Convert to (C)elsius or (F)ahrenheit? ").upper()

# Convert the temperature
if choice == 'C':
    result = (temp - 32) * 5 / 9
    print(f"{temp}°F is equal to {result:.2f}°C")
elif choice == 'F':
    result = (temp * 9 / 5) + 32
    print(f"{temp}°C is equal to {result:.2f}°F")
else:
    print("Invalid choice")
