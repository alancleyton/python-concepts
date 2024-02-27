'''
There are several ways to format strings in python, one of them is
using formatted string literals(also called f-strings for short).

f-strings let you include the value of Python expressions inside a string by prefixing
the string with f or F and writing expressions as {expression}.
'''
from math import pi

name = 'John'
print(f'Hello, my name is {name}!')

# f-strings allows optional format specifier that can be used to format the value.
print(f'The value of pi is approximately {pi:.3f}.') # pi value with three places after the decimal

# Basic usage of the str.format() method
print('My favorite fruit is {}!'.format('apple'))

# A number in the brackets can be used to refer to the position of the object passed into the format() method.
print('I have one {1} and two {0}'.format('dogs', 'cat'))

# If keyword arguments are used in the str.format() method, their values are referred to by using the name of the argument.
print('My name is {first_name} {last_name}'.format(first_name="John", last_name="Doe"))