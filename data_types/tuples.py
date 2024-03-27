'''
In Python, tuples are used to store multiple data types in a single immutable variable.
'''

# tuples can be created enclosed in brackets () and each item is separated by commas
fruits = ('apple', 'banana', 'cherry', 'orange')
print(fruits)

# also can be created using the tuple() method to create a empty tuple
empty_tuple = tuple()
print(empty_tuple)

# accessing a element of the tuple using index
print(fruits[1]) # banana

# tuple with different data types
user = ('John Doe', 26, 'Developer', True)
print(user)
