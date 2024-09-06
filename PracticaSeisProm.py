""" 
se piden 3 calificaciones, asi como el nombre del alumno, se promedian las calificaciones, si el promedio es mayor que 70 
se escribe "aprobado" si es menor que 70 "se escribe reprobado"
"""
#Constructor
class Calificaciones:
	def __init__(self):
		self.c1 = 0
		self.c2 = 0
		self.c3 = 0
		self.n = ""

#promedio
	def promedio(r):
		r = (cal.c1 + cal.c2 + cal.c3)/3
		return r

#comparacion 
	def comparar(self, num):
		if num > 69 and num < 101:
			x = "aprobado"
		elif num < 70 and num > 0:
			x = "reprobado"
		else:
			x = " - Error, su calificacion no esta entre 0 y 100 "
		return x  

cal = Calificaciones()

cal.n = input(" - Ingresa el nombre del usuario: ")
cal.c1 = int(input(" - Ingrese la primera calificacion del alumno "+cal.n+": "))
cal.c2 = int(input(" - Ingrese la primera calificacion del alumno "+cal.n+": "))
cal.c3 = int(input(" - Ingrese la primera calificacion del alumno "+cal.n+": "))

p = cal.promedio()
c = cal.comparar(p)

print(" - ",cal.n," Con calificaciones de: ",cal.c1,", ",cal.c2,", ",cal.c3," con un promedio de ",p," esta ",c)

