# tutorial 4
# special methods allow us emulate special behaviours in python
# they include __init__(), __repr__(), __str__(), __len__() and __add__() functions


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

    # special methods
    # these generates representations of specific string objects
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay


emp_1 = Employee('Hempire', 'Joe', 50000)
emp_2 = Employee('Catsy', 'Kate', 60000)

print(emp_1.__repr__())

print(emp_1.__str__())

# makes ise of the arithmetic addition special method
print(emp_1 + emp_2)

# other special methods
# fullname length
print(emp_2.fullname().__len__())
