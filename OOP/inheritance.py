# Filename: inheritance.py
# Description: Python class Inheritance
# Date: 02-03-2024

# Inheritance: allow to inherit attributes and methods from a parent class
# We can ovewrite or add new functionality


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


# Developer class 
# It inherits Employee class
class Developer(Employee):
    raise_amount = 1.10
    
    # Add a programming language to this class
    def __init__(self, first, last, pay, prog_lang):
        # This is going to past first, last and pay.
        # Use this instead of writing self.first and blablabla all over again
        # Employee.__init__(self, first, last, pay) // This also works
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
    

# Manager class 
# With a list of employees that the manager supervises
class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        self.employees = employees
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    # Method to append employee
    def append_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    # Method to remove employee
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    # Method to print all the employee under this supervisor management
    def print_employee(self):
        for emp in self.employees:
            print(emp.fullname())
        

# Create an instance
dev_1 = Developer("John", "Wick", 50000, "Python")
dev_2 = Developer("John", "Doe", 80000, "Java")

dev_1.apply_raise()
print(dev_1.prog_lang)


# Create a manager
mgr_1 = Manager("Jane", "Doe", 100000, [dev_1])
mgr_1.append_emp(dev_2)
mgr_1.print_employee()