#Preguntas al final del codigo
class Vehiculo:
    def __init__(self, id):
        self.id = id
        self.disponibilidad = "disponible"

class Localizable:
    def __init__(self):
        self.gps = 0

class BicicletaElectrica(Vehiculo,Localizable):
    def __init__(self, id):
        Vehiculo.__init__(self, id)
        Localizable.__init__(self)
        self.bateria = 100
    def disponible(self):
        print(f"Tu vehiculo esta {self.disponibilidad} ")
    def mover(self):
        self.bateria -= 5
        self.gps += 1
        print(f'''ID del vehiculo {self.id}
Tu vehciulo tiene {self.bateria}% de bateria
Tu vehiculo avanzo {self.gps} kilometros''')


class ScooterElectrico(Vehiculo,Localizable):
    def __init__(self, id):
        Vehiculo.__init__(self, id)
        Localizable.__init__(self)
        self.bateria = 100
    def checkLicencia(self):
        licencia = str(input("Tienes licencia? (S/N)"))
        if licencia == "S":
            return True
        else:
            print("No puedes usar este vehiculo!")
            return False

    def mover(self):
        self.bateria -= 10
        self.gps += 1
        print(f''' ID del vehiculo {self.id}
Tu vehciulo tiene {self.bateria}% de bateria
Tu vehiculo avanzo {self.gps} kil ometros''')
ident = input("Cual es el id de tu vehiculo?: ")

scooter = ScooterElectrico(ident)
bicicleta = BicicletaElectrica(ident)

eleccion = 0
while input != 3:
    print('''----------- Menu -----------
    Que vehiculo esta utilizando
    
    1. Scooter Electrico
    
    2. Bicicleta Electrica
    
    3. Salir''')
    eleccion = int(input("Eliga una opcion: "))
    if eleccion == 1:
        if scooter.checkLicencia() == False:
            print("No puedes usar este vehiculo!")
            break
        else:
            print("Bienvenido!")
            scooter.mover()

    if eleccion == 2:
        bicicleta.disponible()
        bicicleta.mover()

    if eleccion == 3:
        print("Gracias por usar nuestro sevicio. Adios!")

    else:
        print("Elija una opcion valida")

'''¿Qué ventajas tiene la herencia múltiple en este ejemplo?
¿Qué posibles problemas puede causar si se usa de forma incorrecta?
¿Por qué se considera que el método mover es polimorfismo?

1. Tiene la ventaja de poder transladas variables y parametros a otras clases.
Nos permite reusar codigo y optimizar procesos para no escribir tanto
2. Se confunde todo y se hace override de cosas que no quieres.
Hace un desmadre en el codigo
3. Porque tiene el mismo nombre pero en diferentes clases'''


