'''
In Python, logical operators are used to combine conditional statements (either True or False).
Python has three logical operators: AND, OR, and NOT.
'''

# AND operator returns True if both the operands are True else it returns False.print(True and True) # True
print(True and True)           # returns True because both operands is true
print(True and True and True)  # returns True because all operands is true
print(True and False)          # returns False because second operand is false
print(True and False and True) # returns False because all operands is not true

# OR operator returns True if either of the operands is True
print(True or False)          # returns True because the first operand is true
print(False or False or True) # returns True because the last operand is true

# NOT operator works with a single boolean value. If the boolean value is True it returns False and vice-versa.
print(not True) # returns False
print(not False) # returns True
