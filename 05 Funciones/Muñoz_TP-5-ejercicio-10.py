def calcular_promedio(a, b, c):
	return (a + b + c) / 3

print("Vamos a calcular el promedio de 3 numeros enteros")
a = int(input("Ingresa el primer numero: "))
b = int(input("Ingresa el segundo numero: "))
c = int(input("Ingresa el tercer numero: "))

promedio = calcular_promedio(a, b, c)

print(f"El promedio entre {a}, {b} y {c} es {promedio}")
