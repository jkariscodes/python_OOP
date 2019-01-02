# tutorial 4
# Inheritance: making use of subclasses to inherit attributes
# from parent classes into child classes


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


# subclass inheriting properties of Employee class
class Developer(Employee):
    def __init__(self, first, last, pay, lang):
        super().__init__(first, last, pay)  # gives us access to inherited methods
        self.lang = lang


# subclass manager inheriting from Employee class
# the manager manages developers
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)  # gives us access to inherited methods
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # assigning manager with ability to add(append) employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    # assigning manager with ability to remove employees
    def rm_emp(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    # method for printing employees' full names
    def print_emps(self):
        for emp in self.employees:
            print(' ', emp.fullname())


# assigning attributes to developer subclass
emp_1 = Developer('hempire', 'joe', 50000, 'Python')
emp_2 = Developer('catsy', 'kate', 60000, '.NET')

# manager attributes
mngr_1 = Manager('Daisy', 'Joey', 90000, [emp_1])
# printing email. email attribute has been inherited from employee to manager
print(mngr_1.email)

mngr_1.add_emp(emp_2)
mngr_1.rm_emp(emp_1)
mngr_1.print_emps()

# testing inheritance
print(emp_1.email)
print(emp_2.lang)

# making use of python in-built functions
# issinstance() checks whether a class/instance is an instance of another class
print(isinstance(mngr_1, Employee))  # returns True
print(isinstance(mngr_1, Developer))  # returns False
# issubclass() checks whether a class/instance is a subclass of another class
print(issubclass(Manager, Developer))  # returns False as Manager is not a subclass of Developer
