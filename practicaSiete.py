#Constructor
class Calificaciones:
	def __init__(self):
		self.c1 = 0
		self.c2 = 0
		self.c3 = 0
		self.n = ""

#promedio
class Promedio(Calificaciones):
	def promedio(r):
		r = (cal.c1 + cal.c2 + cal.c3)/3
		return r

#comparacion 
class comparacion(Promedio):
	def comparar(self, num):
		if num >= 70 and self.c1 >= 70 and self.c2 >= 70 and self.c3 >= 70:
			if num <= 100 and self.c1 <= 100 and self.c2 <= 100 and self.c3 <= 100:
				x = "aprobado"
			else:
				x = "incorrecto su promedio, no puede ser mayor a 100"
		else:
			x = "reprobado"
		return x  

cal = Calificaciones()
prom = Promedio(Clificaciones)
comp = comparacion(Promedio)

cal.n = input(" - Ingresa el nombre del usuario: ")
cal.c1 = int(input(" - Ingrese la primera calificacion del alumno "+cal.n+": "))
cal.c2 = int(input(" - Ingrese la primera calificacion del alumno "+cal.n+": "))
cal.c3 = int(input(" - Ingrese la primera calificacion del alumno "+cal.n+": "))


p = Promedio(Calificaciones).promedio
c = comparacion(promedio).comparar(p)

print(" - ",cal.n," Con calificaciones de: ",cal.c1,", ",cal.c2,", ",cal.c3," con un promedio de ",p," esta ",c)
