# tutorial 2
# distinguishing between class and instance variables
# implementing employee pay rise using class variables


class Employee:
    # class attributes
    num_of_emps = 0
    raise_amount = 1.04

    # class constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@nairobi.com'

        Employee.num_of_emps += 1

    # method for printing full names
    # instance method making use of self
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # pay rise
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Hempire', 'Joe', 50000)
emp_2 = Employee('Catsy', 'Kate', 60000)

# assigning new values
Employee.raise_amount = 1.05
emp_2.raise_amount = 1.04

print(Employee.num_of_emps)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
