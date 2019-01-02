# tutorial 3
# distinguishing between class and instance methods
# making use of decorators for class and instance methods


class Employee:
    raise_amount = 1.04

    # class constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@nairobi.com'

    # method for printing full names
    # instance method making use of self
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # pay rise
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod  # decorator for class method
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # below class creates new employee based on prev employee strings below
    @classmethod
    def from_string(cls, emp_str):  # alternative constructor for employee details
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # method for checking if a given day is a weekday
    @staticmethod  # decorator for static method
    def is_workday(day):
        # checking if day is Saturday (5) or Sunday (6)
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True


emp_1 = Employee('Hempire', 'Joe', 50000)
emp_2 = Employee('Catsy', 'Kate', 60000)

# dummy employee data
emp_str1 = 'Matthew-Anderson-70000'
emp_str2 = 'Simon-Peter-40000'
emp_str3 = 'Caroline-Moore-100000'

# parsing dummy employee values
new_emp_1 = Employee.from_string(emp_str1)
new_emp_2 = Employee.from_string(emp_str2)
new_emp_3 = Employee.from_string(emp_str3)

print(new_emp_3.email)
print(new_emp_2.pay)
print(new_emp_1.first)

# importing the datetime module
from datetime import date

# date in Y-M-D format from datetime module
my_date = date(2019, 1, 1)

print(Employee.is_workday(my_date))
