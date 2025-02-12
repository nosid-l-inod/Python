# List and string slicing
# list[start:end:step]
# 1. start is inclusive 
# 2. end is exclusive

numbers = [12, 3, 23, 1, 4, 65, 64, 33, 443]
name = "john"

# One way to get the last element in the list
last_element = numbers[-1]

# Whole list
whole = numbers[:]

# Reverse string
reverse_name = name[::-1]
print(reverse_name)