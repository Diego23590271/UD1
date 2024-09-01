class Triangulo:
	def __init__(self, b, h):
		self.b = b
		self.h = h
	def area(self):
		r= (self.b * self.h)/2
		return r
ba = float(input(" Ingrese la base del triangulo: "))
ha = float(input(" Ingrese la base del triangulo: "))
triangulo = Triangulo(ba, ha)
print (" El area del triangulo con la base de ",ba," y altura de ",ha," es: ",triangulo.area())

