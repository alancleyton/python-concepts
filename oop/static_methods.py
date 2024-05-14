'''
Static methods in python are methods that belongs to a class, not its instances.
It does not require an instance of the class to be called and don't have access to an instance reference.
'''

class User:
    def __init__(self, name):
        self.name = name

    # static method doesn't receive any reference
    @staticmethod
    def unknown():
        return User('unknown')
    
    # static method with arguments
    @staticmethod
    def capitalized(name):
        return User(name.upper())


user = User('John')
print(user.name) # John

unknown_user = User.unknown() # unknown
print(unknown_user.name)

capitalized_user = User.capitalized('Adam')
print(capitalized_user.name)