# the dir() function returns a list of attributes in a specified object
str_object = 'hello'
print(dir(str_object))

# the hasattr() function checks if a specific attribute exist in object
print(hasattr(str_object, 'upper')) # True
print(hasattr(str_object, 'uppercase')) # False

# the getattr() function returns the value of the specified attribute in a object
str_object_upper_attr = getattr(str_object, 'upper')
print(str_object_upper_attr()) # HELLO
