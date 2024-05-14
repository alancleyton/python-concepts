'''
Access modifiers in Python control the visibility and accessibility of class attributes and methods.
They indicates to other classes can access, modify, or inherit an attribute or method.
Python provides three types of access modifiers: Public, Protected(_) and Private(__).

    - Unlike others object-oriented languages, such as C++ and Java,
    In Python, access modifiers are conventions, not strict enforcement.
'''

class Student:
    # public class attribute
    school_name = None

    def __init__(self, name, age):
        # public instance attributes, are accessible from anywhere outside or inside the class
        self.name = name
        self.age = age

class Person:
    __id = None

    def __init__(self, name, age):
        # protected instance attributes, are accessible within the class and its sub-classes, cannot be accessed outside the class
        # attributes starting by underscore (_) indicates that the attribute is protected
        self._name = name
        self._age = age
    
    # public getter method
    @property
    def name(self):
        return self._name
    
    # private class method, are only accessible within the class, cannot be accessed outside the class or its sub-classes
    # attributes starting by double underscore (__) indicates that the attribute is private
    def __display(self):
        pass

person = Person('John', 41)
print(person.name) # John
print(person._name) # John
person.__display() # AttributeError