# Filename: classes.py
# Description: python classes in python
# Date: 01-03-2025

# Methods are functions inside the class


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


# Call methods
print(emp_1.fullname())
print(emp_1.email)

print(f"\nEmp_1 details: {emp_1.__dict__}")

