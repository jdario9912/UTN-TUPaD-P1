"""
Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es
"""


def es_palindromo(palabra):
    if palabra[0] != palabra[len(palabra) - 1] or not palabra:
        return False
    else:
        inicio = 0 + 1
        final = len(palabra) - 1
        if inicio > final:
            return True
        else:
            return es_palindromo(palabra[inicio:final])


palabra = input("Palabra: ")

print(es_palindromo(palabra))
