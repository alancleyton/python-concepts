'''
In programming you often need to know if an expression is True or False.
'''

'''
You can evaluate any expression in Python, and get one of two answers, True or False.
When you compare two values, the expression is evaluated and Python returns the Boolean answer:
'''
print(10 > 9)
print(10 == 9)
print(10 < 9)

'''
You also can evaluate values and variables.
The bool() function allows you to evaluate any value, and give you True or False in return,
'''
print(bool("Hello"))
print(bool(""))
print(bool(15))
print(bool(0)) # Any number is True, even negatives numbers, except 0