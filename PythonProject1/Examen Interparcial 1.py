'''1. Crea una clase llamada Empleado con los siguientes atributos:

   Nombre del empleado

   Salario por hora

   Salario por hora extra

  Registro de horas trabajadas



La clase Empleado debe tener al menos los siguientes métodos:

   Un método para registrar la información del trabajador

   Un método para calcular el salario, considerando las horas extras.

   Un método para mostrar toda la información del empleado.



3. Implementa las siguientes reglas:

 Las horas trabajadas se pagan normal y las horas extras se pagan a 1.5 veces la tarifa normal. (Considera que una jornada normal de trabajo son 40hrs  a partir de la siguiente hora se considera hora extra.



4. Desarrolla un programa principal que permita:

Registrar la información de un empleado.
Calcular y mostrar el salario de un empleado.
Mostrar detalle de lo trabajado ( x hr trabajadas a $ = total ) + (x hrs extras * $ )  =  ingreso total


Reiniciar el registro de horas para una nueva semana.


El programa debe tener un menú que permita al usuario realizar todas estas operaciones.

--- Menú salario de Empleados ---

1. Motsrar informacion de empleado

2.-Mostrar salario total

3. Mostrar el detalle

4. Reiniciar semana

5. Salir'''


class Empleado:
    def __init__(self, nombre, salario, horas, extra):
        self.nombre = nombre
        self.salario = salario
        self.horas = horas
        self.extra = extra

    def Registrar_empleado(self):
        print(f'''El nombre del empleado es {self.nombre}
Su salario es {self.salario}
Trabajo {self.horas} horas
con {self.extra} horas extra''')
    def Mostrar_Salario_Total(self):
        print(f'''El salario del empleado {self.nombre} es {(self.salario * self.horas) + (self.salario * self.extra * 1.5)}''')

    def Mostrar_a_detalle(self):
        print(f'''El nombre del empleado es {self.nombre}
Su salario es {self.salario}
Trabajo {self.horas} horas
con {self.extra} horas extra
Su salario neto es:{(self.salario * self.horas) + (self.salario * self.extra * 1.5)} 
Siendo {(self.salario * self.horas)} de horas regulares y {(self.salario * self.extra * 1.5)} de horas extra''')

    def Reiniciar_Semana(self):
        "El reinicio ha sido exitoso"
        self.nombre = None
        self.salario = None
        self.horas = None
        self.extra = None
        print("El reinicio ha sido exitoso")
        self.nombre = input("Nombre del empleado: ")
        self.salario = float(input("Salario del empleado: "))
        self.horas = int(input("Horas que trabajo: "))
        if horas1 >= 40:
            self.extra = int(input("Horas extra que trabajo: "))
        else:
            self.extra1 = 0




nombre1 = input("Nombre del empleado: ")
salario1 = float(input("Salario del empleado: "))
horas1= int(input("Horas que trabajo: "))
if horas1 >= 40:
    extra1 = int(input("Horas extra que trabajo: "))
else:
    extra1 = 0


empleado1 = Empleado(nombre1,salario1,horas1,extra1)
opcion = 0

while opcion != 5:
    print('''1. Mostrar informacion de empleado

2.-Mostrar salario total

3. Mostrar el detalle

4. Reiniciar semana

5. Salir''')
    opcion = int(input("Ingresa tu opcion: "))
    if opcion == 1:
        empleado1.Registrar_empleado()

    if opcion == 2:
        empleado1.Mostrar_Salario_Total()

    if opcion == 3:
        empleado1.Mostrar_a_detalle()

    if opcion == 4:
        empleado1.Reiniciar_Semana()

    if opcion == 5:
        print("Hasta Luego!")
        break

    else:
        print("Ingresa una opcion valida")

