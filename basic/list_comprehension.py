# List comprehension
# Simple ways to manage lists

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Copy a list
new_list = [n for n in list]
print(list)

# Double elements
other_list = [n*n for n in list]
print(other_list)

# Get even numbers
even_list = [n for n in list if n % 2 == 0]
print(even_list)


n = [n for n in range(10)]