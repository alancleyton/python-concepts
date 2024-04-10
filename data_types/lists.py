'''
In Python, lists are used to store multiple data type in a single variable
'''

# lists can be created enclosed in [] and each item is separated by commas
fruits = ['apple', 'banana', 'cherry', 'orange']
print(fruits)

# also can be created using the list() to create a empty list
empty_list = list()
print(empty_list) # []

# accessing a element of the list using index
print(fruits[1]) # banana
print(fruits[2]) # cherry

# list with different data types
user = ['John Doe', 26, 'Developer', True]
print(user)

# lists in Python are mutable, the elements of the list can be modified or replaced
user[0] = 'John Wick'
print(user)

# adding elements to the end of the list using the append() method
fruits.append('watermelon')
print(fruits)

# adding an element in a specific position of the list using the insert() method
fruits.insert(1, 'kiwi')
print(fruits)

# extending list adding multiple elements at the end of the list by another list with extend() method
fruits.extend(['pineapple', 'tangerine'])
print(fruits)

# removing an element from the list using the pop() method, by default it removes only the last element of the list.
fruits.pop()
print(fruits)

# removing an element from a specific position of the list passing the index of the element to the pop() method
fruits.pop(0)
print(fruits)

# pop() method also returns the removed element from the list
removed_fruit = fruits.pop(1)
print(removed_fruit) # banana

# copying a list using copy() method
fruits_copy = fruits.copy() # copy() method returns a copy of the list
print(fruits_copy)

# removing a specific element from list using remove() method
fruits.remove('cherry')
print(fruits)

# removing all elements from list using clear() method
fruits.clear()
print(fruits)

# iterating lists
numbers = [12, 3, 6, 42, 22]
for number in numbers:
  print(number)
