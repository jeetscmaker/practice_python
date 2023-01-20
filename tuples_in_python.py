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

# Tuple
tuple_1 = ('History','Civics','Geography','Botany')
tuple_c = tuple_1
print(tuple_1, tuple_c)

''' this will throw an error because tuple is immutable.
 tuple_c[0] = 'Math' 
 similarly we can not append or remove items from a tuple.
 But we can access the element of a tuple. 
'''
print(tuple_c[0])

'''
	Sets in python are data structure which do not allow duplicates.
	they are enclosed within curly brackets.
	Also sets are unordered. That means items are not stored in certain order
	therefore we can't access the items using index.
'''
set_1 = {'History','History', 'Geography'}
print(set_1)  # prints {'History', 'Geography'}