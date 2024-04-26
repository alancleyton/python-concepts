'''
In Python, the __init__.py file is used to to initialize the package when it is imported.
When imported, the __init__.py is implicitly executed, and all the objects inside it can be accessible in the package namespace. 
'''

# all the functions from the maths module is exported to the utils_pkg package namespace
from utils_pkg.maths import *
