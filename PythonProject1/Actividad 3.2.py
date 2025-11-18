print("Bienvenidx!")
opcion = 0
while opcion != 5:
    print('''Menu:
    1. Suma hasta N numeros
    2. Multiplos de 3
    3. Promedio de Grupo
    4. Factorial de un Numero
    5. Salir''')
    opcion = int(input("Seleccione una opcion "))
    if opcion == 1:
        n_inicial1 = int(input("Ingrese el numero inicial: "))
        n_final1 = int(input("Ingrese el numero final: "))
        if n_final1 < n_inicial1:
            print("Numero no valido")
        else:
            suma1 = 0
            for i in range(n_inicial1, n_final1, 2):
                suma1 = suma1 + i
            print("La suma es ",suma1)
    elif opcion == 2:
        print("Ingrese un numero y sumara todos los numeros menores multiplos a 3")
        n_inicial2 = int(input("Ingrese el numero deseado: "))
        if n_inicial2 >= 3:
            for i in range(1, n_inicial2+1):
                if n_inicial2 % 3 == 0:
                    suma2 = n_inicial2 + i
                else:
                    continue
            print("La suma de los numeros es", suma2)
        else:
            print("Pon un numero mayor a 3")
    elif opcion == 3:
        N_Estudiantes = int(input("Cuantos estudiantes tiene el grupo?"))
        suma = 0.0
        for i in range(0,N_Estudiantes):
            calificacion = float(input(f"Escribe el Promedio del estudiante {i+1}:"))
            suma += calificacion

        if N_Estudiantes > 0:
            promedio = suma / N_Estudiantes
            print("El promedio es ", promedio)
        else:
            print("No pueden haber menos de un estudiante")

    elif opcion == 4:
        print("Escribe un numero y te devolvera el factorial de ese numero")
        n_incial3 = int(input("Ingrese el numero deseado:  "))

        suma3 = 1
        if n_incial3 < 0:
            print("Numero no valido")
        else:
            for i in range(1, n_incial3 + 1):
                suma3 *= i
        print(f"el factorial de {n_incial3} es: {suma3}")

    elif opcion == 5:
        print("Saliendo")
    else:
        print("Ingresa una opcion valida")

