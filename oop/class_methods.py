'''
The classmethod() function is used to return the class method for the given function. 
'''

class Student:
    school_name = 'ABC School'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # class methods must have a reference to a class object as the first parameter
    def change_school_name(cls, name):
        cls.school_name = name

# convert change_school_name() to class method with classmethod() built-in function
Student.change_school_name = classmethod(Student.change_school_name)
Student.change_school_name('XYZ School')

student = Student(name='John', age=18)
print(student.school_name)


# create factory method using class class methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def age_from_birth_year(cls, name, birth_year):
        return cls(name, 2024 - birth_year)

person = Person.age_from_birth_year('Adam', 1997)
print(person.name, person.age)