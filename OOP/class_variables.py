# Filename: classe_variables.py
# Description: Class variables
# Date: 21-02-2025

# Class variables are variables that are shared among all instances of a class
# Access class variables: Class_name.variable_name or self.variable_name
# self.variable_name: Allows to change the variable for each instance
# class_name.variable_name: does not allow to change the variable for each instance

# Instance variables - (self.variable_name) can be modified for each instance
# Class variables - (class_name.variable_name ) cannot be modified outside the class



# Create employee class
class Employee:
    
    # Class variable
    number_of_employees = 0
    raise_amount = 1.04
    
    # Init method: runs every time we create an employee
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        # Track the number of employees created
        # Use class_name.variable_name since we dont need to change this
        Employee.number_of_employees += 1
    
    # Method to return full name
    def fullname(self):
        return f"{self.first} {self.last}"
    
    # Method to apply raise using class variable
    # Use self.variable_name since we want to change the value in a given instance
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# Create an instance
emp_1 = Employee("John", "Wick", 5000)

# Apply the raise method
emp_1.apply_raise()

# Change emp_1 raise amount
emp_1.raise_amount = 1.05

# Display the number of employee
print(f"Total number of employees: {Employee.number_of_employees}")
