# Program to display powers of 2 using anonymous function

# Input the number of terms
n_terms = int(input("Enter the number of terms: "))

# Display powers of 2 using lambda and map
powers_of_2 = list(map(lambda x: 2 ** x, range(n_terms)))

# Display the result
print(f"Powers of 2 up to {n_terms} terms are: {powers_of_2}")
