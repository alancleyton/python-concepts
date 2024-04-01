'''
The split() method split a string into a list using a chosen separator.

The split() method receives 2 opitional parameters:
- separator witch specifies the delimiter used to split the string, default separator is any whitespace.
- maxsplit which determines the maximum number of splits, default value is -1.
'''

text = 'I love Python'

# splits using space
splitted_text = text.split()
print(splitted_text)

description = 'Hello, my name is John, I am 27 years old'

# splits using comma and space
splitted_description = description.split(', ')
print(splitted_description) 

fruits = "apple#banana#cherry#orange"

# splits using the maxsplit parameter
# maxsplit: 1
print(fruits.split('#', 1))

# maxsplit: 2
print(fruits.split('#', 2))

# maxsplit: 5
print(fruits.split('#', 5))

# maxsplit: 0
print(fruits.split('#', 0))