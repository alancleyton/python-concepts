'''
The isinstance() function is used to check if the object is of specified type.
Returns True if the specified object is of the specified type, otherwise False.
'''

# receives the OBJECT that need to be checked at first parameter and the CLASS which object is needed to be checked at second parameter
print(isinstance(2, int)) # True
print(isinstance('hello', int)) # False

# checking multiple types passing a  tuple of classes at second parameter
print(isinstance('world', (int, float))) # False
print(isinstance(3.5, (int, float, str))) # True

list_of_types = ['hello', 2, 4, 1.5, 0.88, True, False, [1, 5, 3]]

# getting only numeric types from the list
numbers = [element for element in list_of_types if isinstance(element, (int, float))]
print(numbers) # [2, 4, 1.5, 0.88, True, False] 