# tutorial 1
# basics of creating and instantiating classes
# a class is a blueprint for creating instances


class Employee:

    # class constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@nairobi.com'

    # method for printing full names
    def fullname(self):
        print('{} {}'.format(self.first, self.last))


emp_1 = Employee('Hempire', 'Joe', 50000)
emp_2 = Employee('Catsy', 'Kate', 60000)

# below results are the same but using different approach
emp_1.fullname()
Employee.fullname(emp_1)
