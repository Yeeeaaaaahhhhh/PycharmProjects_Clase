'''menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee',
        "price": 2.50},
    3: {"name": 'cake',
        "price": 2.79},
    4: {"name": 'soup',
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}

def calculate_subtotal(order):
    """Calculates the subtotal of an order"""
    print('Calculating bill subtotal...')
    # Sum all item prices
    subtotal = sum(item["price"] for item in order)
    return round(subtotal, 2)


def calculate_tax(subtotal):
    """Calculates the tax of an order"""
    print('Calculating tax from subtotal...')
    tax = subtotal * 0.15
    return round(tax, 2)


def summarize_order(order):
    """Summarizes the order"""
    print_order(order)
    subtotal = calculate_subtotal(order)
    tax = calculate_tax(subtotal)
    total = round(subtotal + tax, 2)
    names = [item["name"] for item in order]
    return names, total


def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = [item["name"] for item in order]
    print(items)
    return order


def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()


def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order


def main():
    order = take_order()
    print_order(order)

    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str(subtotal))

    tax = calculate_tax(subtotal)
    print("Tax for the order is: " + str(tax))

    items, total = summarize_order(order)
    print("Items ordered:", items)
    print("Total amount due:", total)


if __name__ == "__main__":
    main()
'''

class ProfesionalSalud:
    def __init__(self, nombre, area):
        self.nombre = nombre
        self.area = area
    def presentarse(self):
        print(f"Hola! Me llamo {self.nombre} y trabajo en el area de {self.area}")
    def atenderpaciente(self):
        print("El paciente esta siendo atendiendo")

class EspecialistaTecnologia():
    def __init__(self, experiencia, sistema):
        self.experiencia = experiencia
        self.sistema = sistema
    def diagnosticarEquipo(self):
        print("Diagnosticando equipo......")
    def mostrarHabilidades(self):
        print(f"Soy {self.experiencia} en {self.sistema}")

class BioingenieroClinico(ProfesionalSalud, EspecialistaTecnologia):
    def __init__(self, nombre, area, experiencia, sistema):
        super().__init__(nombre, area)
        super().__init__(experiencia, sistema)

    def mostrarPerfil(self):
        print(f'''Nombre: {self.nombre}
Area: {self.area}
Experiencia: {experiencia}
Sistema: {sistema}''')

    def presentarse(self):
        print(f'''Hola! Me llamo {self.nombre} y trabajo en el area de {self.area}.
Soy {experiencia} en {sistema} y me gustan los changos''')

nombre = input("Cual es tu nombre?: ")
area = input("Cual es tu area?: ")
experiencia = input("Cual es tu experiencia? (Junior o Senior): ")
sistema = input("Cual es tu sistema que manejas?: ")
bioingenieroClinico = BioingenieroClinico(nombre, area, experiencia, sistema)
bioingenieroClinico.mostrarPerfil()
bioingenieroClinico.presentarse()








