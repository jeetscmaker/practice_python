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

# using [key] to access a dict will throw an error if the key is not in dict.
# therefore we can use get() method of dict and also provide a default value in case
# the key is not present in the dict.
print(student.get('phone')) # prints None
print(student.get('phone', 'phone number not found!')) 