from class_methods import Employee

class Developer(Employee):
	def __init__(self, first_name, last_name, salary, prog_lang):
		super().__init__(first_name, last_name, salary)
		# Employee.__init__(first_name, last_name, salary) # alternative to the super() call
		self.programming_language = prog_lang

class Manager(Employee):
	def __init__(self, first_name, last_name, salary, employees = None):
		super().__init__(first_name, last_name, salary)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			employees.append(emp)
	
	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)		
			
	def print_emps(self):
		for emp in self.employees:
			print("-->", emp.full_name())

dev_1 = Employee.from_string("Jane-Alan-1500")
print(dev_1.full_name())

dev_2 = Developer('Shawn', 'Herd', 1200, 'Java')
print(dev_2.programming_language)

manager_1 = Manager('Steve', 'Smith', 2000, [dev_1, dev_2])
Manager.print_emps(manager_1)