class Corredor:
    def __init__(self, numero, nombre, tiempo):
        self.numero = numero
        self.nombre = nombre
        self.tiempo = tiempo

class Carrera:
    def __init__(self):
        self.corredores = []

    def agregar_corredor(self, numero, nombre, tiempo):
        corredor = Corredor(numero, nombre, tiempo)
        self.corredores.append(corredor)

    def mostrar_todos(self):
        print("\n--- Lista de corredores ---")
        for c in self.corredores:
            print(f"Número: {c.numero}, Nombre: {c.nombre}, Tiempo: {c.tiempo}")

    def mostrar_ganador(self):
        ganador = min(self.corredores, key=lambda x: x.tiempo)
        print(f"\n Ganador: {ganador.nombre} (N° {ganador.numero}) con tiempo {ganador.tiempo}")

    def mostrar_mas_lento(self):
        mas_lento = max(self.corredores, key=lambda x: x.tiempo)
        print(f"\nMás lento: {mas_lento.nombre} (N° {mas_lento.numero}) con tiempo {mas_lento.tiempo}")

    def mostrar_promedio(self):
        promedio = sum(c.tiempo for c in self.corredores) / len(self.corredores)
        print(f"\nPromedio de tiempos: {promedio:.2f}")


def main():
    carrera = Carrera()
    n = int(input("Ingrese la cantidad de corredores: "))

    for i in range(n):
        print(f"\nCorredor {i+1}")
        numero = int(input("Número del corredor: "))
        nombre = input("Nombre del corredor: ")
        tiempo = float(input("Tiempo en carrera: "))
        carrera.agregar_corredor(numero, nombre, tiempo)

    carrera.mostrar_todos()
    carrera.mostrar_ganador()
    carrera.mostrar_mas_lento()
    carrera.mostrar_promedio()

if __name__ == "__main__":
    main()
