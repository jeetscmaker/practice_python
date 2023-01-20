''' Dictionary in python is like Map in Java and c++
	so basically they are key-value pair. The key can be any
	immutable data type such as string or int.
'''
student = {} # an empty student dictionary
student  = dict() # same as previous statement.
student = {'name': "John", 'age': 19, 'courses': ['Math', 'CompSci']}
print(student)
print(student['name']) # prints John
print(student['courses']) # ['Math', 'CompSci']