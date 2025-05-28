"""
Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)
"""


def suma_digitos(n):
    return 0 if n == 0 else (n % 10) + suma_digitos(n // 10)


num = int(input("Ingresa un numero: "))

print(suma_digitos(num))
