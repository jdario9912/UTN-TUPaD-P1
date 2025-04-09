max = 100
count = 0
count_pares = 0
count_impares = 0
count_negativos = 0
count_positivos = 0

print(f"Ingresa {max} numeros")
print("")
while count < max:
    num = int(input())
    count = count + 1
    
    if num % 2 == 0:
        count_pares = count_pares + 1
    else:
        count_impares = count_impares + 1
        
    if num > 0:
        count_positivos = count_positivos + 1
    elif num < 0:
        count_negativos = count_negativos + 1
    else:
        pass
    
print("")
print(f"Numeros pares: {count_pares}")
print(f"Numeros impares: {count_impares}")
print(f"Numeros positivos: {count_positivos}")
print(f"Numeros negativos: {count_negativos}")