'''
In Python, a package is a collection of modules organized in a directory
'''

# import a module from the package
import utils_pkg.maths
print(utils_pkg.maths.sum(5, 5))

# import specific module from the package using the (from) keyword
from utils_pkg import maths
print(maths.multiply(2, 20))

# import specific method from the package module
from utils_pkg.maths import divide
print(divide(50, 2))

# import functions from the module inside the package using the __init__
import utils_pkg
print(utils_pkg.multiply(10, 5))