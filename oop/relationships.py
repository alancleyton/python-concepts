'''
Association defines a relationship between two classes which is established through their objects.
It is used to represent a weak connection between two objects. Objects can exist independently in this relationship.
It can be one-to-one, one-to-many, many-to-one, or many-to-many.
'''

# both Course and Student classes are associated with each other
# a student can enroll in multiple courses, but the two classes are independent objects
class Course:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name

class Student:
    _courses = []

    def __init__(self, name):
        self._name = name

    @property
    def courses(self):
        return self._courses

    @courses.setter
    def courses(self, course):
        self._courses.append(course)

student = Student('Adam')
course_1 = Course('Mathematics')
course_2 = Course('Marketing')

student.courses = course_1.name
student.courses = course_2.name

print(student.courses)

'''
Aggregation is a specialized form of association between two or more objects which each object
can exist independently but one object contains or is composed of another object.

It is "whole-part" or "parent-child" relationship, where one object represents the "whole/parent",
and the other object represents a "part/child" of that "whole/parent".
'''

# the Car class aggregates Wheel class objects which a Car may contains Wheels
# but Wheels aren't limited to being a part of a Car and can exist on their own

class Wheel:
    def __init__(self, brand):
        self._brand = brand
    
    @property
    def brand(self):
        return self._brand

class Car:
    def __init__(self, model, year):
        self._model = model
        self._year = year
        self._wheels = []
    
    @property
    def wheels(self):
        return [wheel.brand for wheel in self._wheels]
    
    @wheels.setter
    def wheels(self, wheel):
        if len(self._wheels) >= 4:
            raise Exception('a {model} {year} can only have 4 wheels.'.format(model=self._model, year=self._year))
        self._wheels.append(wheel)

goodyear = Wheel('Goodyear')
bridgestone = Wheel('Bridgestone')
continental = Wheel('Continental')
michelin = Wheel('Michelin')
pirelli = Wheel('Pirelli')

sedan = Car('Toyota', 2004)
sedan.wheels = goodyear
sedan.wheels = bridgestone
sedan.wheels = continental
sedan.wheels = michelin
# sedan.wheels = pirelli
print(sedan.wheels)

'''
Composition is a specialized form of aggregation where one class is integrated into another as a part of its internal structure.
It is a "whole-part" or "parent-child" relationship, where if the "whole/parent" is destroyed, then the "part/child" or also cease to exist.
'''

# a Library may housing one or more Books, if the Library is destroyed
# then all of the Books that are part of the Library are also destroyed

class Book:
    def __init__(self, name, author):
        self._name = name
        self._author = author
    
    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

class Library:
    def __init__(self):
        self._books = []
    
    def addBook(self, name, author):
        self._books.append(Book(name, author))

    @property
    def books(self):
        return [(book.name, book.author) for book in self._books]

lib = Library()
lib.addBook('12 Rules for Life: An Antidote to Chaos', 'Jordan B Peterson')
lib.addBook('Atomic Habits', 'James Clear')
print(lib.books)