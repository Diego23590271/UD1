
class Rectangulo:
	"""Define un rectangulo segun su base y su altura"""
	def __init__(self, b, h):
		self.b = b
		self.h = h
	def area(self):
		return self.b * self.h
ba = float(input(" Ingrese la base del rectangulo: "))
ha = float(input(" Ingrese la base del rectangulo: "))
rectangulo = Rectangulo(ba, ha)
print (" El area del rectangulo con la base de",ba," y altura de ",ha," es: " ,rectangulo.area())


