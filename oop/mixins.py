'''
A mixin is a class that provides a specific set of behaviors or functionality that can be easily implemented into other classes.
- Allows to use one particular feature in a lot of different classes.
'''

class Animal:
    def make_sound(self): # method to be implemented by subclasses
        pass

class CatSoundMixin(Animal):
    def make_sound(self): # implement sound for cats
        return 'cat goes Meow!'

class DogSoundMixin(Animal):
    def make_sound(self): # implement sound for dogs
        return 'dog goes Woof!'

class Cat(CatSoundMixin):
    pass

class Dog(DogSoundMixin):
    pass

cat = Cat()
dog = Dog()
print(cat.make_sound())
print(dog.make_sound())
