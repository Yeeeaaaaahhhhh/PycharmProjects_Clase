'''Crear una función que reciba un parámetro n y cuente cuántos números pares e impares hay entre 1 y n'''

def contador ():
    n = int(input("Ingresa un numero: "))
    contador_par = 0
    contador_impar = 0
    for i in range(n):
        if i % 2 == 0:
            contador_par += 1
        else:
            contador_impar += 1
    print(f'''Hay {contador_par} numeros pares
Hay {contador_impar} numeros impares''')

'''Crear una función que no reciba parámetros pero sea capaz de pedir
 5 números y agregarlos a una lista  y nos diga cual fue el número mínimo de la lista'''

def listaN ():
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))
    num3 = int(input("Ingresa el tercer numero: "))
    num4 = int(input("Ingresa el cuarto numero: "))
    num5 = int(input("Ingresa el quinto numero: "))
    lista1 = [num1, num2, num3, num4, num5]
    print(f"El numero con menor valor de su lista es {min(lista1)}")

'''Crear un menú para ejecutar cualquiera de estas funciones hasta que el usuario diga salir'''

opcion = 0
while opcion != 3:
    print('''Bienvenido al menu del quizz! Elija una opcion
    1. Pregunta 1
    2. Pregunta 2
    3. Salir''')
    opcion = int(input("Ingresa una opcion: "))
    if opcion == 1:
        contador()

    if opcion == 2:
        listaN()

    if opcion == 3:
        print("Saliendo...")
        break

    else:
        print("Ingresa una opcion valida")
