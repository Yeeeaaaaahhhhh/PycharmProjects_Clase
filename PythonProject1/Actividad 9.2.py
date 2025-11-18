'''Elabora una clase llamada Persona :

Sus atributos son: nombre, edad, INE,

Los métodos que se implementaran son:

datos() capturar nombre y edad

esMayorDeEdad(): indica si es mayor de edad

generaINE(): genera un número aleatorio de 8 cifras,

imprimir() la información de los métodos

Crear una clase Empleado que heredará de la clase Persona

Sus atributos: heredada todo del padre y

 además también tendrá: Departamento donde trabaja, horasTrabajadas y pagoPorHora

Los métodos que se implementaran son:

calcular Sueldo

Y deberá heredar los métodos para imprimir toda la información del padre y el hijo

Crea otra  clase Estudiante que también heredará de la clase Persona

Los atributos propios son universidad y  semestre

Capturar la información

Imprimir toda  la información (incluye lo heredado)

Crea el principal

Crea un ciclo  que pregunta que opción va capturar

1.- Empleado

2.- Estudiante

3.- salir

Llame a los métodos correspondientes en cada opción'''
import random
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def datos(self):
        self.nombre = input("Dime tu nombre: ")
        self.edad = int(input("Dime tu edad: "))

    def esMayordeEdad(self):
        mayordeedad = False
        if self.edad >= 18:
            mayordeedad = True
            print("Eres mayor de edad: ")
        else:
            mayordeedad = False
            print("No eres mayor de edad: ")

    def GenerarIne(self):

        ine = []
        self.ine = ine
        for i in range(9):
            numero = random.randint(0,9)
            ine.append(numero)
        return self.ine

    def imprimir(self):
        print(f"Tu nombre es {self.nombre}, tu edad es {self.edad} y tu ine es {self.ine[1]}{self.ine[2]}{self.ine[3]}{self.ine[4]}{self.ine[5]}{self.ine[6]}{self.ine[7]}{self.ine[8]}")

class Empleado(Persona):
    def __init__(self, nombre, edad,horas,pagoxhora):
        super().__init__(nombre, edad)
        self.horas = horas
        self.pagoxhora = pagoxhora
    def calcularSueldo(self):
        self.horas = int(input("Dime tu horas trabajadas: "))
        self.pagoxhora = int(input("Dime tu pago x hora trabajada: "))
        self.sueldo = self.horas * self.pagoxhora
        return self.sueldo
    def imprimirhijo(self):
        print(f"{persona.imprimir()} Tu sueldo es {self.sueldo} ")

class Estudiante(Persona):
    def __init__(self, nombre, edad, universidad, semestre):
        super().__init__(nombre, edad)
        self.universidad = universidad
        self.semestre = semestre
    def imprimirestudiante(self):
        self.universidad = input("Dime tu universidad: ")
        self.semestre = int(input("Dime tu semestre: "))
        print(f"{persona.imprimir()}, Tu universidad es {self.universidad}, Tu semestre es {self.semestre}")


persona = Persona("",18)
persona.datos()
persona.esMayordeEdad()
persona.GenerarIne()
persona.imprimir()

empleado = Empleado("",18,8,8)
empleado.calcularSueldo()
empleado.imprimirhijo()

estudiante = Estudiante("",18,"","")
estudiante.imprimirestudiante()