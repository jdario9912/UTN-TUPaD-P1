import math

acc = 0
modulador = 1

num = int(input("Ingresa un numero entero positivo: "))

bandera = num

while bandera > 10:
    modulador = modulador * 10
    bandera = math.trunc(bandera / 10)

while True:
    if num == 0:
        break   
    
    unidad = num % 10
    acc = acc + unidad * modulador
    modulador = math.trunc(modulador / 10)
    num = math.trunc(num / 10) 

print(f"Numero invertido: {acc}")
