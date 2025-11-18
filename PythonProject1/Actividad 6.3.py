class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura
    def calcular_perimeter(self):
        return (2*self.base) + (2*self.altura)

print("===== Calcula tu Rectangulo =====")
base1 = int(input("Base: "))
altura1 = int(input("Altura: "))

rectangulo1 = Rectangulo(base1,altura1)
print(rectangulo1.calcular_area())
print(rectangulo1.calcular_perimeter())

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        return self.radio * (3.1416**2)
    def calcular_perimeter(self):
        return (2*3.1416*self.radio)

print("===== Calcula tu Circulo =====")
radio = int(input("Radio: "))

circulo1 = Circulo(radio)
print(circulo1.calcular_area())
print(circulo1.calcular_perimeter())

def cola():
    n = 10
    m = 20
    print(n,m)


cola()