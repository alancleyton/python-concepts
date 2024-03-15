'''
In Python, the identity operators are used to compare objects based on their identity.
Everything in Python is an object, and each object has its own unique id. The id is assigned to the object when it is created.
'''

a = 10
b = 10

# id() function returns the identity of an object
# both a and b have the same id because they is pointing to the same object(value)
print(id(a))
print(id(b))

# == returns True because both variables have the same object(value)
print(a == b)

# IS operator returns True because both objects have the same id
print(a is b) # True

'''
The difference between IS and ==:
IS will return True if both variables is pointing to the same objects(values) in memory.
== will return True When the variables have the exact same value.
'''