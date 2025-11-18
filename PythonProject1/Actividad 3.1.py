'''Simulador de cajero automatico
Constuir un menu
1. Consultar Saldo
2. Depositar
3. Retirar
4. Salir
'''
print("Ejercicio 1:")
print("Bienvenido al cajero automatico banqrochido")
opcion = 0
Saldo = 1000
while opcion != 4:
    print('''Menu:
    1. Consultar Saldo
    2. Depositar
    3. Retirar
    4. Salir''')
    opcion = int(input("Ingresa una opcion : "))
    if opcion == 1:
        print(f"Hola! Tu saldo es de {Saldo}")
    elif opcion == 2:
        Deposito = int(input("Ingresa el monto que quiere depositar: "))
        if Deposito < 0:
           print("No te pases de lanza no puedes depositar dinero negativo")
        else:
            Saldo = Saldo + Deposito
            print(f"El deposito ha sido un exito. Su nuevo saldo es de {Saldo}")

    elif opcion == 3:
        Retiro = int(input("Ingresa el monto que quiere retirar: "))
        if Retiro > Saldo:
            print("No tiene suficientes fondos")
        else:
            Saldo = Saldo - Retiro
            print(f"El retiro ha sido exitoso. Su nuevo saldo es de {Saldo}")
    elif opcion == 4:
        print("Saliendo...")
    else:
        print("Elige una opcion valida")

#Ejercicio 2

print("Ejercicio 2:")
sectreto = 2
guess = 0
while guess != 2:
    guess = int(input("Adivina adivinador el numero que estoy pensando del 1 al 20: "))
    if guess < 2:
        print("Tu numero es muy pequeño")
    elif guess == 2:
        print("Felicidades! El numero secreto es 2!")
    elif guess > 20:
        print("Numero no valido")
    else:
        print("El numero es uy grande")

#Ejercicio 3
print("Ejercicio 3:")
print("Adivina Adivinador aleatorio")

from random import*
Aleatorio = randint(1,100)
guess = 0
while guess != Aleatorio:
    guess = int(input("Adivina adivinador el numero que estoy pensando del 1 al 20: "))
    if guess < Aleatorio:
        print("Tu numero es muy pequeño")
    elif guess == Aleatorio:
        print(f"Felicidades! El numero secreto es {Aleatorio}!")
        break
    elif guess > 100:
        print("Numero no valido")
    else:
        print("El numero es muy grande")