def operaciones_basicas(num1, num2):
	return (num1 + num2, num1 - num2, num1 * num2, num1 / num2)

num1 = 34
num2 = 2

resultados = operaciones_basicas(34, 2)

print(f"{num1} + {num2} = {resultados[0]}")
print(f"{num1} - {num2} = {resultados[1]}")
print(f"{num1} * {num2} = {resultados[2]}")
print(f"{num1} / {num2} = {resultados[3]}")
