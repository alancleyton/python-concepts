'''
Closure is a function that remembers values in enclosing scopes even after the outer function has finished executing.
- Outer function: A function that contains another function, can take arguments and define variables.
- Inner function: Function defined within the outer function, can access variables from the outer function even after the outer function has completed execution.
'''

# outer function
def multiplier(f):
  # inner function
  def multiply(x):
    return x * f
  return multiply

# inner function reference to a variable with outer function enclosing scope
double = multiplier(2)
triple = multiplier(3)

print(double(10)) # 20
print(triple(50)) # 150

def counter():
  count = 0
  def increment():
    nonlocal count  # nonlocal indicate we're modifying the count variable in the outer scope
    count += 1
    return count
  return increment

counter1 = counter()
print(counter1())  # 1
print(counter1())  # 2