#Parent class
class Cat:

	#Class attribute
	species = "Common European"

	#Initializer intence attributes
	def __init__(self, name, age):
		self.name = name
		self.age = age

	#instance method
	def description(self):
		return (f"{self.name} have {self.age} years old.")

	#instance method
	def speak(self, sound):
		return (f"{self.name} says {sound}")

#Child class(inherits from Cat class)
class Siames(Cat):
	"""docstring for Siames"""
	def run(self, speed):
		return (f"{self.name} runs {speed}")

#Child class(inherits from Cat class)
class Persa(Cat):
	"""docstring for Siames"""
	def run(self, speed):
		return (f"{self.name} runs {speed}")

"""Child classes inherit attributes and 
	behaviors from the parent class"""

haku = Siames("Haku", 12)
print(haku.description())

"""Child classes inherit attributes and 
	behaviors as well"""
print(haku.run("slowly"))