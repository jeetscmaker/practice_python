message = "Hello World."
print(message)

message2 = "Hello World with double quotes"
print(message2)

message3 = """multiline strings in python start
and end with triple quotes."""
print(message3)

length_of_string = len(message3)
print("length of 'multiline strings in python start and end with tripe quotes.' is = " + str(length_of_string))

# print the first character of message2
print("The first char of message2 is = " + message2[0])

# print the first 5 characters (from index 0 to index 4) of message2
print("First 5 characters of message2: " + message2[0:5])
# same output even if we remove 0 i the range because by default it counts from 0th index.
print("First 5 characters of message2: " + message2[:5])

# start from the 6th index and print till the end of message2
print("Starting from 6th index till the end of message2: " + message2[6:])

# print message2 to lowercase
print(message2.lower())

# print message2 to uppercase
print(message2.upper())

# But message2 remains intact because string is immutable.
print(message2)

# count the number of 'l' in message3
print(message3.count('l'))
