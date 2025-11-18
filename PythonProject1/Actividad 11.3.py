def Cociente(a,b):
    try:
        resultado = (a / b)
        print(resultado)
    except ZeroDivisionError:
        print("El segundo argumento no debe ser 0")
    except TypeError:
        print("Los argumentos deben ser numeros")

a = (input("Introduce un numero: "))
b = (input("Introduce un numero: "))
Cociente(a,b)

