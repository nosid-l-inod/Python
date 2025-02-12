# For loop

# break -> to stop the loop
# continue -> to skip elements

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# For to iterate the array
for i in numbers:
    if i == 7:
        print("Found!")
        break # Break in 7
    elif i == 3:
        continue # Skip 3
    print(i)
    
    
    
# range
print("\n")
for i in range(1, 10):
    print(i)
