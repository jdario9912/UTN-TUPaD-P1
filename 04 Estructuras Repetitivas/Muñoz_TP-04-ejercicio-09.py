max = 3
count =  0
acc = 0

print(f"Ingresa {max} numeros para calcular la media")
print("")

while count < max:
    num = int(input())
    acc = acc + num
    count = count + 1

print("")
print(f"Media: {acc / max}")