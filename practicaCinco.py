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
ba = float(input(" Ingrese la base del rectangulo: "))
ha = float(input(" Ingrese la base del rectangulo: "))
rectangulo = Rectangulo(ba, ha)
print (" El area del rectangulo con la base de",ba," y altura de ",ha," es: " ,rectangulo.area())

ba = float(input(" Ingrese la base del triangulo: "))
ha = float(input(" Ingrese la base del triangulo: "))
triangulo = Triangulo(ba, ha)
print (" El area del triangulo con la base de ",ba," y altura de ",ha," es: " ,triangulo.area())

print(" El area del rectangulo es de ", rectangulo.area())
print(" El area del triangulo es de ", triangulo.area())


"""tarea: crear un menu para que el usuario indique si nececita el area del triangulo o del rectangulo"""
