'''
	List is a mutable data structure in python.
	Tuple is an immutable data structure.
	Let's understand the mutability of a list using few examples.
'''
list_1 = ['History', 'Civics', 'Geography', 'Botany']
list_c = list_1
print(list_1, list_c)

# Altering the list_c now to see that the changes are also reflected in list_1
list_c[0] = 'Geology'
print(list_1, list_c)

# Tuple
tuple_1 = ('History', 'Civics', 'Geography', 'Botany')
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
set_1 = {'History', 'History', 'Geography'}
print(set_1)  # prints {'History', 'Geography'}

set_math = {'Math', 'Physics', 'Chemistry', 'CompSci'}
set_art = {'Math', 'Economics', 'Design'}

# print the intersection of set_math and set_art
print(set_art.intersection(set_math))  # prints {'Math'}

# print the difference between the sets
print(set_art.difference(set_math))  # prints {'Economics', 'Design'}

# print the combination of sets
# {'Math', 'Economics', 'Physics', 'CompSci', 'Design', 'Chemistry'}
print(set_art.union(set_math))

# Creating list
l = []
l = list()

# Creating tuple
t = ()
t = tuple()

# Creating set
s = {}  # this is not right. It is a dictionary not a set.
s = set()  # correct

# unpacking a tuple into variables
my_tuple = 1, 2, 3
x, y, z = my_tuple
print(f"x = {x}, y = {y}, z = {z}")
