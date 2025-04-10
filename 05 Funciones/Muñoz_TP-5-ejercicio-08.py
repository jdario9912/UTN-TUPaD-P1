import math

def calcular_imc(peso, altura):
	imc = peso / altura
	return math.trunc(imc * 100) / 100

print("Calculo de IMC")
print("")
peso = float(input("Ingresa tu peso: "))
altura = float(input("Ingresa tu altura: "))

imc = calcular_imc(peso, altura)
print("")
print(f"Segun tu peso {peso} y altura {altura}, tu IMC es {imc}")
