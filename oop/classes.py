'''
In Python, almost everything is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
'''

# create a new class using the ´class´ keyword
class Person:
    # class property
    current_year = 2024

    # use the .__init__() method as the object initializer to define and sets the initial values for object attributes
    # the first argument of most methods in classes is ´self´, this argument holds a reference to the current object that can be used inside the class
    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    # class object method
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
    
    # method to change first_name property
    def change_first_name(self, new_first_name):
        self.first_name = new_first_name
    
    def get_birth_date(self):
        return self.current_year - self.age

# create a new Person object instance
person = Person('John', 'Doe', 27)

# access the values of the Person object properties
print(person.first_name)
print(person.last_name)
print(person.get_full_name())

# change the class object properties
person.first_name = 'Will'
print(person.first_name)
print(person.get_full_name())

# change the class object properties with class method
person.change_first_name('Adam')
print(person.first_name)
print(person.get_full_name())

print(person.get_birth_date())