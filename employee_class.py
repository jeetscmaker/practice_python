class Employee(object):
	
	def __init__(self, first_name, last_name, salary):
		self.fname = first_name
		self.lname = last_name
		self.sal = salary
		self.email = first_name + '.' + last_name + '@company.com'

	def full_name(self):      # This argument 'self' is very important
		return '{} {}'.format(self.fname, self.lname)		

emp_1 = Employee("John", "Dalton", 1000)
emp_2 = Employee("Ray", "Palmer", 1500)

print(emp_1.full_name())         # emp1 is automatically passed as self.
print(emp_2.full_name())
print(emp_1.email)
print(emp_2.email)
print(Employee.full_name(emp_1)) # another way of passing argument to self.
print(Employee.full_name(emp_2))
print(emp_1.__dict__)
print(Employee.__dict__)