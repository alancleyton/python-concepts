'''
inheritance is one of the core concepts in oop. It is a feature that allows us to create a new class from an existing one.
- The newly created class is known as the subclass (child or derived class).
- The existing class from which the child class inherits is known as the superclass (parent or base class).
- Python has a builtin object superclass which is the base for all classes. All classes inherit from it.
'''

# superclass or parent class
class Person:
    uid = '1234'

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def get_full_name(self) -> str:
        return self.first_name + ' ' + self.last_name

# superclass or child class
class Student(Person):
    def __init__(self, first_name, last_name, age):
        # access the superclass methods and attributes using super() function
        super().__init__(first_name, last_name)
        self.age = age
        
    def print_fullname(self):
        print(self.first_name, self.last_name)
    
    def get_full_name_upper(self):
        # using superclass methods
        full_name = super().get_full_name()
        return full_name.upper()

john = Student('John', 'Doe', 18)
john.print_fullname()

# access superclass attribute
print(john.uid)
print(john.age)
print(john.get_full_name())
print(john.get_full_name_upper())


