# Lists are indexed based data structure which are mutable.
nums = [1,2,3,4,5]
print(nums)

# a =             [7, 2, 6, 9, 11] 
# index =          0  1  2  3  4
# reverse index =  -5 -4 -3 -2 -1
# a[:] gives a shallow copy of the original list.
# Above operation is called sicing of list. Few Examples of slicing:
# a[0:3] gives [7,2,6] excluding the value at 3rd index.
# a[-5:-1] gives [7,2,6,9,] exlusing the value at -1th index
# a[2:] gives [6,9,11]
# a[-2] gives [9,11]

nums_copy = nums[:]
print(nums_copy)
print(nums_copy[-2:])
print(nums[:4])
print(nums[1:3])

# mutable list, that means internal value of a list can be changed.
squares = [1,4,9,15,25] # the square of 4 should be 16 but it is 15
squares[3] = 16
print(squares)

more_squares  = squares + [36,49]
print(more_squares)

more_squares.append(64)
print(more_squares)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)
# now remove them
letters[2:5] = []
print(letters)
# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)

# The built-in function len() also applies to lists:
letters = ['a', 'b', 'c', 'd']
print(len(letters))

# It is possible to nest lists (create lists containing other lists), for example:
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])

''' list can also waork as 'Stack' data structure
# there is no push() function in list as of today.
# we can use append() to add an element at the end of the list.
# but a pop() removes and returns last element from the list.
'''
letter_d = letters.pop() # returns 'd'
print(letter_d, letters) # now letters = ['a', 'b', 'c']

# We can also inplace reverse a list using reverse()
letters.reverse()
print(letters)

# We can also inplace sort a list in ascending order using sort() function
letters.append('d') # letters = ['c', 'b', 'a', 'd']
letters.sort()      # letters = ['a', 'b', 'c', 'd']
print(letters)

# sort a list in descending order
primes = [11, 3, 7, 29, 19, 31, 5]
primes.sort(reverse=True)
print(primes)   # [31, 29, 19, 11, 7, 5, 3]

''' If we don't want to alter the original list by sorting then we can 
    get a copy of the sorted list by using sorted() function. '''
sorted_primes = sorted(primes)
print(sorted_primes)  # [3, 5, 7, 11, 19, 29, 31]

# finding minimum of a list
minimum = min(primes)
maximum = max(primes)
sum_of_list = sum(primes)
print(minimum, maximum, sum_of_list)

# we can find the first index of an item using index() method
print(primes.index(5))
print("Anthony".index('n'))

# to find the occurrence of an item in a list
print(4 in primes) # returns False
print('p' in "Anthony") # returns False
print('y' in "Anthony") # returns True

# enumerate over a list using enumerate() print index and its corresponding value.
courses = ['Math', 'Physics', 'Chemistry', 'CompSci']
for index, value in enumerate(courses):
	print(index, value)

# if we don't want the index to start from 0, then we can pass a start value of index
for index, value in enumerate(courses, start = 1):
	print(index, value)

# if we want to join the values in our list using a delimeter
delimeter = ', '
print(delimeter.join(courses)) # Math, Physics, Chemistry, CompSci
print('-'.join(courses))       # Math-Physics-Chemistry-CompSci