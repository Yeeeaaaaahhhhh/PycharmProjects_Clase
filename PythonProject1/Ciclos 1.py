print('Ejercicio 1')
entero1 = int(input("Ingresa tu entero entero mayor que 1: "))

#inicializamos variable del while
i = 1
while i <= entero1:
    print(i)
#Incremento de la variable
    i = i+1

#Suma positivos hasta que ingrese un numero negativo
print('''Ejercicio 2
Suma numeros positivos para sumar o negativos para restar''')

#incializamos acumulador
suma = 0
numero2 = 0
while numero2 >= 0:
    numero2 = int(input("Ingresa un numero positivo : "))
    if numero2 >= 0:
        suma += numero2
    else :
        suma -= numero2

print(f"La suma total es {suma}")

#Ejercicio 3
print('Ejercicio 3: Menu Interactivo')
opcion = 0
while opcion != 3:
    print('''Menu:
    1. Saludar
    2. Numero al cuadrado
    3. Salir:''')
    opcion = int(input("Ingresa una opcion : "))
    if opcion == 1:
        print("Ola q me ves lo feo q te ves")
    elif opcion == 2:
        numero3 = int(input("Ingresa un numero : "))
        numero3 = numero3**2
        print(f"El numero es {numero3}")
    elif opcion == 3:
        print("Bye bye")
    else:
        print("Elige una opcion valida")

