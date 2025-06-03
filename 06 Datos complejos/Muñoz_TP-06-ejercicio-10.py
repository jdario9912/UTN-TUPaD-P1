original = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Colombia": "Bogotá",
}

invertido = {}

paises = list(original.keys())

for pais in paises:
    capital = original[pais]
    invertido[capital] = pais

print(invertido)
