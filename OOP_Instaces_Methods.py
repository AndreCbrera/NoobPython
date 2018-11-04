class Cat(object):
	"""Class attribute"""
	species = 'comun europeo'
	"""docstring for dogs"""
	def __init__(self, name, age):
		super(Cat, self).__init__()
		self.name = name
		self.age = age
		
	"""Instance method"""
	def description(self):
		return (f"{self.name} have {self.age} years old")
		"""Instance method"""
	def speak(self, sound):
		return (f"{self.name} says {sound}")

"""Instantiate the CAT object"""
haku= Cat("Haku", 2)

"""Call our instance methods"""
print(haku.description())
print(haku.speak("meow meoww"))