'''
Recursion is the process that happens when a function is called within itself.
Is used to divide a large problems into smaller, easier to solve, sub-problems.
'''

# countdown recursive function
def recursion(n):
  return n if n == 1 else recursion(n - 1)

print(recursion(50))

# fibonacci sequence
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(9))

def fat(n):
  if n <= 1:
    return n
  else:
    return n * fat(n - 1)
  
print(fat(6))