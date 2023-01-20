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

# adding key-value to dict
student['phone'] = '999-999-9999'

# removing key-value from a dict
del student['age']
print(student) # age-19 key value pair deleted

pho = student.pop('phone') # phone key pair removed and value stored in pho.
print(pho, student)

# print the length of dict
print(len(student))

# print all the keys of dict
print(student.keys())

# print all the values of dict
print(student.values())

# print all the key-value pairs in dict
print(student.items())

# iterating through the keys of dict
for every in student:
	print(every) # prints only keys

# iterating through key-value pair
for key, value in student.items():
	print(key, value)