class alumno:
	def __init__(self):
		self.nombre = "Diego"
	def saludar(self):
		"""imprime un saludo en pantalla"""
		print (f" Hola, {self.nombre}")

x = alumno
x.saludar()
print(x.nombre)
