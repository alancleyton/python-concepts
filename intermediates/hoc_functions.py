'''
Higher order functions are functions that can take another function as an input argument or returns functions as output.
'''

# function passed to another function as arguments
def message(func, text):
  return func(text)

def to_upper(text):
  return text.upper()

some_message = message(to_upper, 'hello world')
print(some_message)



def double_to_each(func, numbers):
  return [func(n) for n in numbers]

def double(x):
  return 2 * x

doubles = double_to_each(double, [1, 2, 3])

print(doubles)