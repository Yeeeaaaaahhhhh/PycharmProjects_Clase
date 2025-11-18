'''Deberás crear un método que se llame mostrar_menú
M E N U
1.- Deposito
2.- Retiro
3.- Salir
Crea un ciclo que permita
llamar al mostrar_menú
Cada opción deberá pedir los datos correspondientes, cantidad a depositar o cantidad a retirar
llamar el método correspondiente de la case
Deberás crear una clase llamada Banco
Que inicializa saldo a 0
Crea un métodos uno abonar
               Suma al saldo
Crea el método retirar
               Debe restar la cantidad indicada al saldo
               Aquí deberás validar que el monto a retirar sea mayor o igual al disponible
               Si no fuera así
                              Deberás mandar un mensaje que diga Saldo insuficiente
Después de cada operación debe mostrar el saldo total
Y mostrar nuevamente el menú'''
class Banco():
    def __init__(self):
        self.saldo = 0
    def depositar(self,deposito):
        self.saldo += deposito
        print(f"Haz depositado {deposito} correctamente")
        print(f"Tu nuevo saldo es: {self.saldo}")
    def retirar(self,retiro):
        if retiro <= self.saldo:
            self.saldo -= retiro
            print(f'''Tu retiro de {retiro} ha sido exitoso
Tu nuevo saldo es: {self.saldo}''')
        else:
            print("No tiene suficiente saldo")

banco = Banco()
opcion = 0
while opcion != 3:
    print (''' --====¡Bienvenido al cajero automatico!====--
    Eliga una opcion para continuar:
    1. Deposito 
    2. Retiro
    3. Salir
    
    ''')
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        deposito = int(input("Ingrese la cantidad del deposito: "))
        banco.depositar(deposito)

    if opcion == 2:
        retiro = int(input("Ingrese la cantidad del retiro: "))
        banco.retirar(retiro)

    if opcion == 3:
        print("Hasta luego!")

    else:
        print("opcion invalida")

