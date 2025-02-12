# Dictionary
# Dictionaries allow to work with key value pairs


# Create a dictionary
student = {"name": "John", "age": 24, "courses": ["Math", "CompSci"]}


# Access a value of a key
# get method handles errors
name = student.get("name")
print(f"Student's name: {name}") 

# Access value that does not exists
# Not found is optional, and will be shown if its not found
# By default in None
height = student.get("height", "Not found")
print(f"Height: {height}")


# Add a value
student["Phone"] = "555-5555"

# Update multiple values 
student.update({"age": 22, "name": "Yasmin"})

# Delete value
del student["age"]

# Length
length = len(student)


# Loop the dictionary
for key, value in student.items():
    print(key, value)