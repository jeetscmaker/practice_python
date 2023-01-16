class Employee(object):
	
	def __init__(self, first_name, last_name, salary):
		self.fname = first_name
		self.lname = last_name
		self.sal = salary
		self.email = first_name + '.' + last_name + '@company.com'

	def full_name(self):
		return '{} {}'.format(self.fname, self.lname)		

emp_1 = Employee("John", "Dalton", 1000)
emp_2 = Employee("Ray", "Palmer", 1500)

print(emp_1.full_name())
print(emp_2.full_name())
print(emp_1.email)
print(emp_2.email)