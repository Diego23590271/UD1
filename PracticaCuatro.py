class alumno:
	def __init__(self,nombre):
		self.nom = nombre
	def saludar(self):
		"""imprime un saludo en pantalla"""
		print (f"Hola, {self.nom} ")
n = input("Ingrese su nombre: ")
x = alumno(n)
x.saludar()
"""print(x.nom)"""

