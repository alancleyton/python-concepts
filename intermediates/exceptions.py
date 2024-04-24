'''
In Python, an exception is a type of error that occurs when an unexpected event occurs during program execution.
Exceptions can be caught and handled by the program with the TRY and EXCEPT block to catch and handle exceptions. 
'''

try:
  # the program terminates as soon as it encounters this error and go to the except block
  divide_by_zero = 7 / 0
except:
  print('is not possible to divide a number by 0')

# python comes with built-in exceptions classes that are raised when errors occur
# we can use thoso classes to handle with specific exceptions
try:
  print(x)
  divide_by_zero = 7 / 0
except NameError:
  print('x variable does not exists')
except ZeroDivisionError:
  print('is not possible to divide a number by 0')
except Exception:
  print('an exception occurred')
  

# get the exception error instance
try:
  my_string = 'hello'
  my_string[0] = 's'
except Exception as error:
  print(error.__class__.__name__, error)
  print('an exception occurred')


# the finally block will be executed if the try block occur an error or not
try:
  print(y)
except:
  print("something went wrong")
finally:
  print("the exception is finished")

# using else keyword to execute a block of code if no errors occur
try:
  sum = 2 + 2
except:
  print("something went wrong")
else:
  print("nothing went wrong")

# throw exceptions with raise keyword to force a specified exception to occur
def double(n):
  if not type(n) is int:
    raise TypeError("only integers are allowed")
  return 2 * n

try:
  double('2')
except TypeError as error:
  print(error) # only integers are allowed
  print("something went wrong with double function")
