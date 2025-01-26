# Python list
# List can store multiple values


# Create a list
nba = ["Warriors", "Celtics", "Lakers", "Dallas"]
numbers = [34, 43, 323, 39, 99, 47]


# Add item to the last position
nba.append("Timberwolves")

# Add items in the first position
nba.insert(0, "Suns")

# Add multiple values to the list
nba.extend(["Thunder", "Rockets"])

# Remove an element
nba.remove("Celtics")

# Remove the last element in the list. It returns the removed value
nba.pop()


# Reverse the list
nba.reverse()

# Sort the list
numbers.sort()

# Sort reversed
numbers.sort(reverse=True)


# Minimum element
minimum = min(numbers)
print(f"Minimum element: {minimum}")

# Maximum element 
maximum = max(numbers)
print(f"Maximum element: {maximum}")

# Sum of the list
sum = sum(numbers)
print(f"List sum: {sum}")

# Length
length = len(numbers)
print(f"List length: {length}")


# Get the index of an element
warrior_index = nba.index("Warriors")
print(f"Warriors' index: {warrior_index}")

# Check if element exists
rockets_in_nba = "rockets" in nba
print(f"Rockets in nba: {rockets_in_nba}\n") 

# Loop the list
for i in nba:
    print(i)
    
# Show elements and include its index
for index, team in enumerate(nba, start=1):
    print(index, team)
    
# Separated by comma (Or space or whatever)
comma = ", ".join(nba)
print(f"Joined list: {comma}")