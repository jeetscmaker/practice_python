import sys

print(sys.version)
print("Hello !!")

# using + for concatenation.
name = "John"
subs = 10000
print("Hello " + name + ", you have " + str(subs) + " subscribers.")

# using f'string for concatenation.
print(f"Hello {name}, you have {subs} subscribers.")
