a = 5
b = 10
c = a + b
print("c is = " + str(c))

# let's declare a = "17", b = 5 and c = a+b
# a = 17
# b = "5"
# c = b+a # TypeError: can only concatenate str (not "int") to str
# d = a+b # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(c)

a = "17"
b = 5
c = a + str(b)  # output will be 175
d = b + int(a)  # output will be 22
print("c is = " + str(c))
print("d is = " + str(d))

a = 5
b = 2
c = a/b  # output will be 2.5
d = a//b # output will be 2, the // operator performs an integer division.
print(c)
print(type(c))  # <class 'float'>
print(d)
print(type(d))  # <class 'int'>