'''
In Python, every file with the .py extension containing Python code that can be imported inside another file is a module. 
'''

# import a module using the (import) keyword
import random
print(random.randint(0, 10))

# add alias to module import using the (as) keyword
import math as m 
print(m.pi)

# import specific parts from the module using the (from) keyword
from sys import platform
print(platform)

# import a module from another file in the same directory level
import fibo as fibo
print(fibo.fib(20))
