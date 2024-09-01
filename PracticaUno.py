"""
"""
"""
class saludo:
    def __init__(self,saludos):
        self.s= saludos
h= saludo("Hola mundo")
print(h.s)
"""

class saludo:
	def __init__(self,saludos):
		self.s=saludos
n=input("Ingrese su nombre: ")
h= saludo("Hola "+n+" Bienvenido")
print(h.s)

