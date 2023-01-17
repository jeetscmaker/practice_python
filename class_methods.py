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

	@classmethod      #decorator for class method
	def set_raise_amount(cls, amount):
		cls.raise_amount = amount

emp_1 = Employee("John", "Dalton", 1000)
emp_2 = Employee("Ray", "Palmer", 1500)

Employee.set_raise_amount(1.06)
print(Employee.raise_amount) # prints 1.06 because of set_raise_amount class method
print(emp_1.raise_amount) # prints 1.06
print(emp_2.raise_amount) # prints 1.06

emp_str_1 = "Don-Monhy-1000"
first_name, last_name, salary = emp_str_1.split('-')
emp_3 = Employee(first_name, last_name, salary)
print(emp_3.full_name())

