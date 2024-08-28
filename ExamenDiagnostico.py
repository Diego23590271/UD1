"""
se pide 3 calificaiones de n alumnos de 0 a 100 asi como el nombre 
del alumno.
se promedia a los alumnos de calificaion menor a 70 se se les imprime un mensaje
de reprobado 
al finalizar el sistema se imprime el nombre y promedio del alumno con mayor calificacion 
y el alumno con menor calificacion
"""
NA = 0
cont = 1


print("         PROMEDIOS       ")
print("                         ")
print("                         ")

NA = int(input("ingrese el numero de alumnos: "))
print("                                          ")

while cont <= NA:
	calif1 = int(input(f"Ingrese la calificación 1 del alumno {cont} : "))
	calif2 = int(input(f"Ingrese la calificación 2 del alumno {cont} : "))
	calif3 = int(input(f"Ingrese la calificación 3 del alumno {cont} : "))
	
	s = calif1 + calif2 + calif3
	p = s/3
	
	print(f"El promedio del alumno {cont} es de ",p," ")

	if (p < 70) and (p >= 0 ):
		print (f"El alumno {cont} esta reprobado ")
		print("                                         ")
	elif (p >= 70) and (p <= 100):
		print (f"El alumno {cont} esta aprobado")
		print("                                         ")
	else: 
		print ("La calificacion o calificaciones estan mal")
		print("                                         ")
		
	cont += 1
