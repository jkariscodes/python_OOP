# tutorial 6
# the @property decorator that returns property object,
# python getter and setter methods


class Employee:

    # class constructor checks the limits of the values
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # enables us access email function as an attribute as well as a method
    @property
    def email(self):
        return '{}.{}@nairobi'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = 'FName'
        self.last = None


emp_1 = Employee('Joe', 'Hempire')
emp_1.fullname = 'GIS Enthusiast'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
print(emp_1.fullname)
