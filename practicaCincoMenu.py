class Poligono:
	"""define un poligono segun su base y su altura"""
	def __init__(self, b, h):
		self.b = b
		self.h = h
class Rectangulo(Poligono):
	def area(self):
		return self.b * self.h 
class Triangulo(Poligono):
	def area(self):
		return (self.b * self.h)/2


print("==============================")
print("=         -Areas-            =")
print("=                            =")
print("=   1. Rectangulo            =")
print("=   2. Triangulo             =")
print("=                            =")
print("==============================")
print("                                ")
M = int(input("Que area desea calcular?  "))
print("                                   ")
if (M == 1):
	ba = float(input(" Ingrese la base del rectangulo: "))
	ha = float(input(" Ingrese la base del rectangulo: "))
	rectangulo = Rectangulo(ba, ha)
	print (" El area del rectangulo con la base de",ba," y altura de ",ha," es: " ,rectangulo.area())
elif (M == 2):
	ba = float(input(" Ingrese la base del triangulo: "))
	ha = float(input(" Ingrese la base del triangulo: "))
	triangulo = Triangulo(ba, ha)
	print (" El area del triangulo con la base de ",ba," y altura de ",ha," es: " ,triangulo.area())
else:
	print("ERROR, ",M," no estadentro de las opciones")



