import datetime as dt


class Employee(object):
    raise_amount = 1.04
    numuber_of_employees = 0

    def __init__(self, first_name, last_name, salary):
        self.fname = first_name
        self.lname = last_name
        self.sal = salary
        self.email = first_name + '.' + last_name + '@company.com'

        # increment the number_of_employees when a new employee is initialized.
        Employee.numuber_of_employees += 1

    def full_name(self):      # This argument 'self' is very important
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        # It must be either Employee.raise_amount or self.raise_amount
        # otherwise it will throw error.
        self.sal = int(self.sal * self.raise_amount)

    @classmethod  # decorator for class method
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first_name, last_name, salary = emp_str.split('-')
        return cls(first_name, last_name, salary)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


emp_1 = Employee("John", "Dalton", 1000)
emp_2 = Employee("Ray", "Palmer", 1500)

Employee.set_raise_amount(1.06)
# prints 1.06 because of set_raise_amount class method
print(Employee.raise_amount)
print(emp_1.raise_amount)  # prints 1.06
print(emp_2.raise_amount)  # prints 1.06

emp_str_1 = "Don-Monhy-1000"
first_name, last_name, salary = emp_str_1.split('-')
emp_3 = Employee(first_name, last_name, salary)
print(emp_3.full_name())

''' creating an employee using from_string class method.
 the class method must be called using the class name followed by dot operator 
 followed by method name. '''
emp_str_2 = "Jane-Alan-1500"
emp_4 = Employee.from_string(emp_str_2)
print(emp_4.full_name())

my_date = dt.date(2023, 1, 15)  # it was a Sunday so returns False.
workday = Employee.is_workday(my_date)
print("my_date was a work day: " + str(workday))

my_date = dt.date(2023, 1, 17)  # it was a Tuesday so returns True.
workday = Employee.is_workday(my_date)
print("my_date was a work day: " + str(workday))
