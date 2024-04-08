'''
In Python, scope specifies the region where we can access avariable.
We can declare variables in two most commonly used general scopes: global scope and local scope.
'''

# global scope variable, available to all code below
name = 'John'

def greet():
  # local scope variable, available only inside the greet() function
  message = 'Hello'
  print(message + ' ' + name)

greet()

