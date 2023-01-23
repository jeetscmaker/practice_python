import sys

print(sys.version)
print("Hello !!")

# using + for concatenation.
name = "John"
subs = 10000
print("Hello " + name + ", you have " + str(subs) + " subscribers.")

# using f'string for concatenation.
print(f"Hello {name}, you have {subs} subscribers.")

# point is an (x, y) tuple
point = -1, 2
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
