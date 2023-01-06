a = 5
b = 10
c = a + b
print("c is = " + str(c))

# let's declare a = "17", b = 5 and c = a+b
a = 17
b = "5"
c = b+a # TypeError: can only concatenate str (not "int") to str
d = a+b # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(c)