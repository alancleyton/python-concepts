'''
Sets in Python are unordered collections used to store unique and immutable elements.
'''

# sets can be created enclosed in {} and each item is separated by commas
names = {'Adam', 'joe', 'Maya', 'Sarah'}
print(names)

# also can be created using the set() to create a empty set
empty_set = set()
print(empty_set)

# sets do not allow duplicate values, duplicate values will be ignored
set_with_duplicated_values = {1, 5, 5, 3, 7, 8, 8, 8, 9, 10, 6}
print(set_with_duplicated_values)

# sets are also iterable
s = {'foo', 'bar', 'baz', 'foo', 'qux'}
for item in s:
  print(item)

# sets are unordered and do not have a index to access an specific element, but as iterable you can check if a specific element exists on set
print('foo' in s) # True
print('baz' not in s) # False

# add elements to the set using the add() method
s.add(100)
print(s)

# modify a set using update() method
s.update(('add', 500))
print(s)

# remove an element from the set using the discard() method
s.discard('qux')
print(s)

# clear the entire set using clear() method
s.clear()
print(s)

# union of two sets without duplicates with | operator
first_set = {1, 2, 3}
second_set = {3, 4, 5}
set_union = first_set | second_set
print(set_union) # {1, 2, 3, 4, 5}

# intersection all the common elements of two sets with & operator
set_intersection = first_set & second_set
print(set_intersection) # 3

# symmetric difference between two sets with - operator
first_set_difference = first_set - second_set
second_set_difference = second_set - first_set
print(first_set_difference) # {1, 2}
print(second_set_difference) # {4, 5}

# difference between two sets with ^ operator
set_symmetric_difference = first_set ^ second_set
print(set_symmetric_difference) 