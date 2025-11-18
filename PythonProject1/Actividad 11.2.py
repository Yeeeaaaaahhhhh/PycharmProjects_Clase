

class Casa:
    def __init__(self, pisos, metros, habitaciones, presupuesto):
        self.pisos = pisos
        self.metros = metros
        self.habitaciones = habitaciones
        self.presupuesto = presupuesto
        self.presupuesto_inicial = presupuesto
        self.valor = (2000 * self.metros) + (5000 * self.habitaciones) + (220000 * self.pisos)
        self.casacomprada = False

    def comprar(self):
        if self.valor <= self.presupuesto:
            print("¡Compra exitosa! Yay!")
            self.presupuesto -= self.valor
            self.casacomprada = True
        else:
            print("Eres pobre, no te alcanza")
        return self.casacomprada

    def pintar(self):
        if self.casacomprada:
            if self.presupuesto >= 45000:
                self.presupuesto -= 45000
                print("¡Pintamos toda la casa!")
                return self.presupuesto
            else:
                print("Eres pobre, no te alcanza ni pa' la pintura")
        else:
            print("Eres pobre, no tienes casa")

    def remodelar(self):
        if self.casacomprada:
            if self.presupuesto >= 100000:
                self.presupuesto -= 100000
                print("¡Remodelamos toda la casa!")
                return self.presupuesto
            else:
                print("Eres pobre, no te alcanza ni pa' remodelar")
        else:
            print("Eres pobre, no tienes casa")


class Auto:
    def __init__(self, marca, ano, presupuestoA):
        self.marca = marca
        self.ano = ano
        self.presupuestoA = presupuestoA
        self.presupuesto_inicialA = presupuestoA
        self.comprarauto = False
        self.valor = 0

    def cotizacion(self):
        self.valor = (self.ano * 1000)
        print(f"El auto está cotizado en {self.valor}")
        return self.valor

    def comprar(self):
        if self.presupuestoA >= self.valor:
            self.presupuestoA -= self.valor
            print(f"¡Has comprado el auto de marca {self.marca}!")
            self.comprarauto = True
        else:
            print("Eres pobre, no te alcanza pa'l carro")
        return self.comprarauto

    def cargar_combustible(self, litros):
        costo_x_litro = litros * 25
        if self.presupuestoA >= costo_x_litro:
            self.presupuestoA -= costo_x_litro
            print("¡Cargaste gasolina con éxito!")
        else:
            print("Eres pobre, no te alcanza ni pa' la gasolina")

    def revision_y_permiso(self):
        if self.presupuestoA >= 5000:
            self.presupuestoA -= 5000
            print("Revisión realizada con éxito")
        else:
            print("Eres pobre, no tienes pa' la revisión")

        if self.presupuestoA >= 1500:
            self.presupuestoA -= 1500
            print("¡Ya tienes permiso!")
        else:
            print("Eres pobre, no tienes pa'l permiso")


class Cliente(Casa, Auto):
    def __init__(self, pisos, metros, habitaciones, presupuesto, marca, ano, presupuestoA, nombre, apellido, edad):
        Casa.__init__(self, pisos, metros, habitaciones, presupuesto)
        Auto.__init__(self, marca, ano, presupuestoA)
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def pago_total(self):
        gasto_casa = self.presupuesto_inicial - self.presupuesto
        gasto_auto = self.presupuesto_inicialA - self.presupuestoA
        pagototal = gasto_casa + gasto_auto
        print(f"El costo total ha sido: {pagototal}")
        print(f"Presupuesto restante total: {self.presupuesto + self.presupuestoA}")


# PROGRAMA PRINCIPAL
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
pisos = int(input("¿De cuántos pisos quiere su casa?: "))
metros = int(input("¿De cuántos metros cuadrados quiere su casa?: "))
habitaciones = int(input("¿De cuántas habitaciones quiere su casa?: "))
presupuesto = int(input("¿Cuál es su presupuesto para la casa?: "))
marca = input("¿De qué marca quiere su vehículo?: ")
ano = int(input("¿De qué año quiere su vehículo?: "))
presupuestoA = int(input("¿Cuál es su presupuesto para el auto?: "))
litros = int(input("¿Cuántos litros quiere cargar a su carro?: "))

casa = Casa(pisos, metros, habitaciones, presupuesto)
auto = Auto(marca, ano, presupuestoA)
cliente = Cliente(pisos, metros, habitaciones, presupuesto, marca, ano, presupuestoA, nombre, apellido, edad)

casa.comprar()
casa.pintar()
casa.remodelar()
auto.cotizacion()
auto.comprar()
auto.cargar_combustible(litros)
auto.revision_y_permiso()
cliente.pago_total()
