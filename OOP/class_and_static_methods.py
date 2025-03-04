# Filename: class and static methods
# Description: Class methods and static methods in python OOP
# Date: 01-03-2024

# Regular methods: take instance (self) as the first argument
# Class methods take class as the first argument (add @classmethods)

# Static methods does not depends on the class (or something like that)
# Static method: dont take the instance or the class as the first argument


# Classmethods: can be used as alternative constructors
# Staticmethods: dont operate in the instance or the class

# Create employee class
class Employee:
    
    number_of_employees = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.number_of_employees += 1
    
    # Method to return full name
    def fullname(self):
        return f"{self.first} {self.last}"
    
    # Method to apply raise using class variable
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Takes a class and amount as argument
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # Method to return if the date is a weekday or not
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 4:
            return False
        return True
        
        

# Create an instance
emp_1 = Employee("John", "Wick", 5000)
emp_2 = Employee("Optimus", "Prime", 8400)

# Change the raise amount, a class variable
# The functions automatically takes the class as an argument, only put the amount
Employee.set_raise_amount(1.6)

print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_1_str = "John-Doe-9000"


# Datething
import datetime
date = datetime.date(2022, 7, 10)

print(Employee.is_workday(date))
