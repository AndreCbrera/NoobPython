class Cat(object):
	"""Class attribute"""
	species = 'comun europeo'
	"""docstring for dogs"""
	def __init__(self, name, age):
		super(Cat, self).__init__()
		self.name = name
		self.age = age
		
"""Cats Objects"""
luna = Cat("Luna", 1 )
mumi = Cat("Mumi", 3 )
haku = Cat("Haku", 5 )

"""Determinates oldest cat"""
def getBiggestNumber(*old):
	return max(old)

"""Access to attributes"""
print("{} tiene {} , {} tiene {}.".format(
	luna.name, luna.age, mumi.name, mumi.age))

"""Race of cat"""
if luna.species == "comun europeo":
	print ("{} es un {}!".format(luna.name, luna.species))

print("El gato mas anciano tiene {} años".format(
	getBiggestNumber(luna.age, mumi.age, haku.age)))