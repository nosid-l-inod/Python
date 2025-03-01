# Filename: even_odd
# Description: Check if number is even or odd
# Date: 21-02-2024


# Get the number
number = int(input("Type the number: "))

# Check if its even or odd
if (number % 2 == 0):
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")