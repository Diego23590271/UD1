
class cajaCambio:
	def __init__(self):
		self.Diez = 0
		self.Cinco = 0
		self.Uno = 0
	
	def comparacion(self, c):
		if c >= 16:
			self.Diez = 1
			self.Cinco = 1
			self.Uno = 1
			c -= 16

		while c > 0:
			if c >= 10:
				self.Diez += 1
				c -= 10
			elif c >= 5:
				self.Cinco += 1
				c -= 5
			else:
				self.Uno += 1
				c -= 1

		return self.Diez, self.Cinco, self.Uno

c = int(input("Introduce la cantidad a convertir: "))

self = cajaCambio()
self.comparacion(c)

print(f"Monedas de 10 pesos: {self.Diez}")
print(f"Monedas de 5 pesos: {self.Cinco}")
print(f"Monedas de 1 peso: {self.Uno}")
	 
	



