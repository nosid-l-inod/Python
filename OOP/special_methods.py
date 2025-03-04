# Filename: special_methods.py
# Description: Special methods in classes
# Date: 02-03-2024


class Employee:
    
    number_of_employees = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.number_of_employees += 1
    
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
        
    # Special methods
    # Display data when we run print(emp_1)
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)


# Create employees
emp_1 = Employee("John", "Wick", 50000)
emp_2 = Employee("John", "Doe", 55000)


print(emp_1)