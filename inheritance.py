from class_methods import Employee

class Developer(Employee):
	pass

dev_1 = Employee.from_string("Jane-Alan-1500")
print(dev_1.full_name())