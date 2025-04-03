# 1
print("Hola Mundo!")

# 2
nombre = input()
print(f"Hola {nombre}!")

# 3
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = int(input("Ingresa tu edad: "))
residencia = input("Ingresa tu lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4
radio = float(input("Ingresa el radio: "))
area = 3.14 * radio ** 2
perimetro = 2 * 3.14 * radio
print(f"Area: {area}")
print(f"Perimetro: {perimetro}")

# 5
segundos = int(input("Ingresa el tiempo en segundos: "))
horas = segundos // 3600
print(f"{segundos} segundos son {horas} horas")

# 6
numero = int(input("Ingresa un numero: "))
print(f"{numero} * 1 = {numero * 1}")
print(f"{numero} * 2 = {numero * 2}")
print(f"{numero} * 3 = {numero * 3}")
print(f"{numero} * 4 = {numero * 4}")
print(f"{numero} * 5 = {numero * 5}")
print(f"{numero} * 6 = {numero * 6}")
print(f"{numero} * 7 = {numero * 7}")
print(f"{numero} * 8 = {numero * 8}")
print(f"{numero} * 9 = {numero * 9}")
print(f"{numero} * 10 = {numero * 10}")

# 7
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")

# 8
altura = float(input("Ingresa tu altura: "))
peso = float(input("Ingresa tu peso: "))
imc = peso / (altura ** 2)
print(f"Tu IMC es: {imc}")

# 9
celcius = float(input("Ingresa la temperatura en Celsius: "))
fahrenheit = (celcius * 9/5) + 32
print(f"Temperatura en Fahrenheit: {fahrenheit}")

# 10
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio es: {promedio}")
