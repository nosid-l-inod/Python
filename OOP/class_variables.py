# Filename: classe_variables.py
# Description: Class variables
# Date: 21-02-2025

# Class variables are variables that are shared among all instances of a class


# Create employee class
class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
    
    # Method to return full name
    def fullname(self):
        return f"{self.first} {self.last}"


# Create an instance
emp_1 = Employee("John", "Wick", 5000)

