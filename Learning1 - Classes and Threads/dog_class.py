class Dog:

	# Class Attribute
	species = 'mammal'

	# Initializer / Instance Attributes
	def __init__(self, name, age):
		self.name = name
		self.age = age

# Instantiate the dog object
philo = Dog("Philo",5)
mikey = Dog("Mikey",6)

#Access the instance attributes
print("{} is {} and {} is {}.".format(philo.name, philo.age, mikey.name, mikey.age))

#Is philo a mammal?
if philo.species == 'mammal':
	print("{0} is a {1}!".format(philo.name, philo.species))

