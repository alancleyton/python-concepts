'''
In Python, getters and setters are not the same as those in other OOPs languages.
The "Pythonic" way to use getters and setters is using the @property decorator to achieve getters and setters.
'''

class Person:
    def __init__(self):
        # naming an attribute starting by underscore indicates that the attribute should only be accessed by the class's internals
        self._name = None
        self._age = None

    # using the @property decorator to create a getter 
    @property
    def name(self):
        return self._name
    
    # using created getter to create a setter
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age

person = Person()

# setting object properties values using getters and setters
person.name = 'John Doe'
person.age = 24
print(person.name, person.age) # John Doe 24