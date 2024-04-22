'''
Lambda functions are small anonymous functions.
They're defined without a name, can take any number of arguments, but can only have one expression.
- Lambda functions are used as an anonymous function inside another function.
- They're also used to create a functioin with simple expressions 
'''

# defining the anonymous function with lambda keyword
multiply = lambda n: 2 * n
print(multiply(2)) # 4

# using lambda with another function
def multiply_by(multiplier):
  return lambda number: multiplier * number

multiply_by_two = multiply_by(2)
print(multiply_by_two(5)) # 10

# declaring and execute a lambda function in a single expression
print(multiply_by(3)(5)) # 15
print((lambda n: 2 * n)(20)) # 40