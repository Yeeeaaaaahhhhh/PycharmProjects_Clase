'''Identifica Clases, atributos y métodos  y preséntalos mediante un diagrama de clases.
Después de tener el diagrama crea el programa que sea capaz de realizar lo siguiente:
Capturar información sobre sus empleados como son el id, nombre sueldoBruto, tipo empleado (A,O).
Se desea saber el descuento de impuestos que tendrá cada empleado, a los tipo A se les descuenta el 30% de impuestos, y a la otra categoría solo el 20% sobre el sueldo bruto.
Además se les entrega una bonificación a todos los empleados del 5% sobre el sueldo bruto.
Después deberá mostrar el sueldo neto del empleado donde le agrega la bonificación y resta los impuestos
Finalmente deberá mostrar todos los datos antes mencionados

El programa deberá ser capaz de solicitar ID, nombre, sueldo bruto y tipo de empleado, además del sueldo bruto.
y deberá mostrar los datos del empleado capturado'''

class empleado:
    def __init__(self, ident, nombre, sueldo,tipoemp):

        self.ident = ident
        self.nombre = nombre
        self.sueldo = sueldo
        self.tipoemp = tipoemp

    def mostrar_datos(self):
        sueldoneto1 = self.sueldo
        sueldoneto2 = sueldoneto1 * 1.05
        if self.tipoemp == "A":
            sueldoneto3 = sueldoneto2 * 0.70
        elif self.tipoemp == "O":
            sueldoneto3 = sueldoneto2 * 0.80
        return sueldoneto3





ident = int(input("Ingrese su ID de trabajador: "))
nombre = input("Ingrese su nombre: ")
sueldo = int(input("Ingrese su sueldo: "))
tipoemp = input("Ingrese su tipo de empleado (A) o (O): ")

empleado1 = empleado(ident, nombre, sueldo, tipoemp)
print(f'''El sueldo neto para el trabajador {nombre}, con el ID {ident} 
y el timpo de empleado {tipoemp} es:
{empleado1.mostrar_datos()}''')