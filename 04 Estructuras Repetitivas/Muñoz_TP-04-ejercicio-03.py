min = 0
max = 0
acc = 0
incremento = 0

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

if num1 < num2:
    min = num1
    max = num2
else:
    min = num2
    max = num1
    
incremento = min + 1

while incremento > min and incremento < max:
    acc = acc + incremento
    incremento = incremento + 1
    

print(acc)