class tablasMultiplicar:
	def __init__(self):
		self.op = 0
		
	def proceso(self, op):
		while op >= 5:
			for i in range(1,11):
				if op == 1:
					print (f" 2 x {i} = {2*i}")
				elif op == 2:
					print (f" 5 x {i} = {2*i}")
				elif op == 3:
					print (f" 8 x {i} = {2*i}")
				elif op == 4:
					print (f" 10 x {i} = {2*i}")
			if op == 5:
				print("Gracias por utilizar nuestro programa ")

		

print("                             ")
print("=============================")
print("=                           =")
print("=          Menú:            =")
print("=     1. Tabla del 2        =")
print("=     2. Tabla del 3        =")
print("=     3. Tabla del 5        =")
print("=     4. Tabla del 10       =")
print("=     5. Salir              =")
print("=                           =")
print("=============================")
    
op = int(input("Seleccione una opción: "))

self = tablasMultiplicar()
self.proceso(op)


print("Programa finalizado.")
