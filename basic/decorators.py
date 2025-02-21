# Decorators in python

# Decorators takes a function as an argument, add some functionality and returns another function
# It does not change the original function

# Allow to add functionalities to existing functions


def decorator(original_function):

    def wrapper():
        print("Before calling the function")
        return original_function()
    
    return wrapper


# Adding more things to the "decorator" function
@decorator
def greet():
    print("Hello")

greet()
