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
