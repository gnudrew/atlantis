# Parent class
class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

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
    Bulldog("Elle Driver", 1, True),
    RussellTerrier("Hattori Hanzo", 3, True),
    Dog("Bill", 7, True)
]

# Instantiate the pets class
my_pets = Pets(my_dogs)

# Output
print("I have {} dogs in the pack.".format(len(my_pets.dogs)))
for i in my_pets.dogs:
    print("{} is {}.".format(i.name, i.age))
print("And they're all {}s!".format(Dog.species))
print('By extension Bulldogs are {}s and Russel Terriers are {}s too!'.format(Bulldog.species,RussellTerrier.species))

# Feed the dogs
for i in my_pets.dogs:
    i.eat()

# Check if all dogs are fed.
all_hungry = True
all_fed = True
for i in my_pets.dogs:
    all_hungry = all_hungry and i.is_hungry
    all_fed = all_fed and not i.is_hungry
if all_hungry:
    print("My dogs are hungry.")
elif all_fed:
    print("My dogs are not hungry.")
else:
    print("Mixed bag.")