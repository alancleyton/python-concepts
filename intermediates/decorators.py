'''
Decorators in Python are functions that allows you to modify or extend an function
across another function without altering the wrapped function's code
'''

# decorator function to returns a string in upper case
def to_uppercase(function):
  def to_uppercase_inner(*args, **kwargs):
    result = function(*args, **kwargs)
    uppercase_string = result.upper()
    return uppercase_string
  return to_uppercase_inner

# applying a decorator to a function with @ symbol (syntactic sugar)
@to_uppercase
def uppercase_string(string):
  return string

print(uppercase_string('hello world'))


# decorator with arguments
def to_plus(number):
  def to_plus_outer(function):
    def to_plus_inner(*args, **kwargs):
      result = function(*args, **kwargs)
      return number * result
    return to_plus_inner
  return to_plus_outer

@to_plus(2)
def sum(x, y):
  return x + y

print(sum(5, 5))