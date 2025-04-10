def celsius_a_fahrenheit(celsius):
	return (celsius * (9/5)) + 32

celsius = float(input("Ingresa una temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius}°C = {fahrenheit}°F")
