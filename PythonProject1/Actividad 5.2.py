

def multiplica ():
    limite1 =  int(input("Ingresa un numero: "))
    acum = 1
    for i in range(limite1):
        acum  = acum * (2*(i+1))
        print(acum)

def sumatoria (limte2):
    suma = 0
    for i in range (limite2):
        suma = suma + (limite2*(i+1))
        print(suma)

def factorial (limite3):
    factorial = 1
    for i in range(limite3):
        factorial = factorial * (i+1)
        print(factorial)

opcion = 0
while opcion != 4:
    print('''Bienvenido al menu! Elige una opcion
    1. Multiplicatoria
    2. Sumatoria
    3. Factorial
    4. Salir''')
    opcion = int(input("Ingresa una opcion: "))

    if opcion == 1:
        multiplica()

    if opcion == 2:
        limite2 = int(input("Ingresa un numero: "))
        sumatoria(limite2)

    if opcion == 3:
        limite3 = int(input("Ingresa un numero: "))
        factorial(limite3)

    if opcion == 4:
        print("Saliendo...")
        break
    else:
        print("Ingresa un numero valido")