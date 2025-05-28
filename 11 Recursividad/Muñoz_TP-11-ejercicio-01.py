"""
Comprensión y aplicación de la recursividad: El estudiante será capaz de definir y
comprender el concepto de recursividad, identificando los casos base y recursivos en
una función recursiva
"""


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Ingresa un numero positivo: "))

for i in range(1, num + 1):
    print(f"factorial: {factorial(i)}")
