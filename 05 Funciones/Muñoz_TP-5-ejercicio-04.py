import math

pi = math.pi

def calcular_area_circulo(radio):
	return pi  * (radio ** 2) * 2

def calcular_perimetro_circulo(radio):
	return pi * radio * 2	

print(calcular_area_circulo(3))
print(calcular_perimetro_circulo(4))
