'''
Dictionaries in Python are collections of key-value pairs.
The dictionary keys must be unique, and the value may be of any type.
'''

# dictionaries are defined by enclosing key:value pairs inside curly brackets {}, separated by commas
frameworks = {
  'python': 'Django',
  'java': 'Spring Boot',
  'ruby': 'Sinatra'
}
print(frameworks)

# also can be created using the dict() to create a empty dictionary
person = dict(name='John', lastname='Doe', age=27)
print(person)

# accessing a item of the dictionary using index
print(person['name']) # John
print(person['lastname']) # Doe

# dictionary with different data types
car = {
  'brand': 'Ford',
  'electric': False,
  'year': 1964,
  'colors': ['red', 'white', 'blue'],
}

# dictionaries in Python are mutable, the elements of the dictionary can be modified or replaced
car[ 'electric'] = True
print(car)

# add new keys and values to dictionary
car['price'] = 20.000
print(car['price'])

# delete keys and values from dictionary
del car['price']
print(car)