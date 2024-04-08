'''
Functions in Python is a block of code that runs a specific task.
Functions are used to increase code readability and reuse, avoiding writing the same code again and again.
'''

# functions are defined with the keyword def, followed by the function name enclosed in parentheses ()
def my_awesome_function():
  print('Hello my awesome Function!')

# use the function name enclosed in parentheses to call a function
my_awesome_function()

# optional inputs can be passed into functions as arguments
def greetings(name):
  print(f'Hello, {name}')

greetings('John')

'''
In Python, arguments can be passed to a function in two ways: positional arguments or keyword arguments:
- Positional arguments (also called required arguments) are passed to a function based on its position in the list of parameters inside the parentheses.
- Keyword arguments are passed to a function by specifying the parameter name and its corresponding value.
'''

def total_price(qty, item, price):
  print(f'{qty} {item} cost ${price:.2f}')

# calling the function with positional arguments
total_price(5, 'bananas', 4.64)

# calling the function with keyword arguments
total_price(item='apples', qty=10, price=23.84)

# function can be called with both positional and keyword arguments
total_price(2, 'notebooks', price=33.54)

# when positional and keyword arguments are passed to a function, all the positional arguments must come first inside the parentheses
# total_price(1, item='tablet', 629.99) # SyntaxError: positional argument follows keyword argument

# function parameters can be defined with a default value
def user(firstname, lastname, age=24):
  print(f"My name is {firstname} {lastname} and i'm {age} years old")

user('john', 'Doe')

# default parameter value can be changed on function call.
user('Tim', 'Martin', 33)

# when a parameter is defined with a default value, all the required parameters must come first inside the parentheses
# def user(firstname, lastname, age=24, id): # SyntaxError: non-default argument follows default argument

'''
Every function in Python has an implicit return value.
If the function doesn't have any return statement, then it returns a None value.
'''
def hello():
  print('Hello!')

hello_function_value = hello()
print(hello_function_value) # None

# function with a return statement to specify a return value
def sum(a, b):
  return a + b

sum_result_value = sum(10, 10)
print(sum_result_value) # 20

# function with an unknown number of arguments using (*), most commonly used as *args by convention
def sum_numbers(*numbers):
  result = 0
  for number in numbers:
    result += number
  return result

print(sum_numbers(5, 5, 100, 20))

numbers = 15, 56, 10, 99
print(sum_numbers(*numbers))