from math import pi

class Circulo:
    def __init__(self, radio):
        self.radio = radio
        
    def calcular_area(self):
        return pi * (self.radio^2)
    
    def calcular_perimetro(self):
        return 2 * pi * self.radio
    
circulo1 = Circulo(5)

print(circulo1.calcular_area())
print(circulo1.calcular_perimetro())