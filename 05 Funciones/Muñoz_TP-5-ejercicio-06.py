def tabla_multiplicar(numero):
	for i in range(1, 11):
		print(f"{i} x {numero} = {i * numero}")

numero = int(input("Ingresa un numero para generar su tabla de multiplicar: "))

tabla_multiplicar(numero)
