"""
1. un numero y su tabla de multiplicar
2. menu 
3. while 
"""

n = int(input(" - Ingrese un numero: "))

for i in range(1,11):
	t = (n*i)
	print (f"{i} x {n} = {t}")


