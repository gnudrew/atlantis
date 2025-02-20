# Parent class
class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())

# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = True

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    # instance method
    def eat(self):
        self.is_hungry = False

    # instance method
    def walk(self):
        return "{} is walking!".format(self.name)

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Create the pack
my_dogs = [
    Bulldog("Tom", 1, True),
    RussellTerrier("Fletcher", 3, True),
    Dog("Larry", 7, True)
]

# Instantiate the pets class
my_pets = Pets(my_dogs)

# Walk the dog pack
my_pets.walk()

