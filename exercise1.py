class Dog:

	# Class Attribute
	species = 'mammal'

	# Initializer / Instance Attributes
	def __init__(self, name, age):
		self.name = name
		self.age = age

# Instantiate 3 dogs
fido = Dog("fido",7)
bones = Dog("bones",2)
bo = Dog("bo",5)

# Get Oldest
def get_max(*args):
    return max(args)

# Report
maxAge = get_max(fido.age, bones.age, bo.age)
print("Oldest doggo is {} years, which is {} in dog years.".format(maxAge, maxAge*7))