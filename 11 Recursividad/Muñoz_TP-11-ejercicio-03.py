"""
Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un
algoritmo general
"""


def potencia(base, pot):
    if pot == 0:
        return 1
    else:
        return base * potencia(base, pot - 1)


base = int(input("Base: "))
potenciar = int(input("Potencia: "))

print(potencia(base, potenciar))
