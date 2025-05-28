"""
Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
"""


def decimal_a_binario(decimal):
    return "" if decimal == 0 else f"{decimal_a_binario(decimal // 2)} {decimal % 2}"


num = int(input("Entero: "))

print(decimal_a_binario(num))
