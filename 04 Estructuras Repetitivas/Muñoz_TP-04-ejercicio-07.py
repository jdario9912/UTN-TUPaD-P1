max = int(input("Ingresa un numero entero positivo: "))
acc = 0

for i in range(max):
    acc = acc + i
    if i + 1 == max:
        break
    
print(acc)