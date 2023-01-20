'''
	List is a mutable data structure in python.
	Tuple is an immutable data structure.
	Let's understand the mutability of a list using few examples.
'''
list_1 = ['History','Civics','Geography','Botany']
list_c = list_1
print(list_1, list_c)

# Altering the list_c now to see that the changes are also reflected in list_1
list_c[0] = 'Geology'
print(list_1, list_c)