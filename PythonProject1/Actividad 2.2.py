print('''Bienvenido! Elige un ejercicio que quieras hacer :)
1. Clasificacion de edad
2. Calificacion de examen 
4. Desicor de beca y reinscripccion''')

Ejercicio = int(input('Ejercicio: '))
match Ejercicio:
    case 1:
        print("Bienvenido a la opcion 1: Clasificacion de edad")
        anio = int(input('En que año naciste_:'))
        edad = 2025-anio

        if edad <= 0 or edad >= 100:
            print("El año escrito no es valido ")
        else:
            if edad <= 12:
                print(f"Tu edad es: {edad}, por lo tanto eres un niño")
            elif edad > 12 and edad <= 18:
                print(f"Tu edad es: {edad}, por lo tanto eres un adolescnete")
            elif edad > 18 and edad <= 60:
                print(f"Tu edad es: {edad}, por lo tanto eres un adulto")
            else:
                print(f"Tu edad es: {edad}, por lo tanto eres un adulto mayor")

    case 2:
        print("Bienvenido a la opcion 2: Calificacion de examen: ")
        calificacion = float(input("Ingresa tu calificacion del 1 al 10"))
        if calificacion == 10 or calificacion >= 9.0:
            print("Eres un alumno excelente")
        elif calificacion <= 8.9 or calificacion >= 7.6:
            print("Eres un buen alumno")
        elif calificacion <= 7.5 or calificacion >= 6.0:
            print("Eres un alumno regular")
        else:
            print("Eres un mal alumno y deberias estar avergonzado")
    case 4:
        print("Bienvenido a la opcion 3: Decisor de beca y reinscripcion: ")
        promedio = float(input("Ingresa tu promedio del 1 al 10"))
        if promedio <= 0 or promedio >= 10:
            print("Promedio escrito no es valido ")
        ingresos = float(input("Ingresa tus ingresos mensuales"))
        if ingresos <= 0:
            print("Eres un alumno muy pobre para la anahuac :(")
        servicio = str(input("Haces servicio social? 'S' o 'N' "))
        adeudos = str(input("Tienes adeudos? 'S' o 'N' "))
        if promedio >= 9.0 and ingresos <= 15000 and adeudos == "N":
            print("Beca Otorgada! Felicidades!")
        elif promedio <= 9.5 and servicio == "S" and adeudos == "N":
            print("Beca Otorgada! Felicidades!")
        else:
            print("Beca no otorgada :(")

        if adeudos == "N":
            print("Reinscripcion permitida!")
        else:
            print("Reinscripcion no permitida")


    case _:
        print("Opcion no valida")
