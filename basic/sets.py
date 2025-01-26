# Sets are unordered and have no duplicates


numbers = {34, 43, 323, 39, 99, 47, 1 , 1}
numbers2 = {1, 2, 453, 22, 333, 54, 23, 43}

# Check common values 
common = numbers.intersection(numbers2)
print(f"Element in common: {common}")

# Differences (element in numbers but not in numbers2)
differences = numbers.difference(numbers2)
print(f"Differences: {differences}")

# Combine
combine = numbers.union(numbers2)
print(f"Combined sets: {combine}")

# Create an empty set
empty_set = set()