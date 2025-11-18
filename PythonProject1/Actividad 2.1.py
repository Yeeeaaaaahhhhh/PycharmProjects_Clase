print("Ejercicio 1")

numero1 = int(input("Ingresa un numero: "))

if numero1 % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

print("Ejercicio 2")

tareas = int(input("Ingresa tu calificacion de tareas: "))
examenes = int(input("Ingresa tu calificacion de examenes: "))
ejercicios = int(input("Ingresa tu calificacion de ejercicios: "))

P_Tareas = tareas * 0.40
P_Examenes = examenes * 0.40
P_Ejercicios = ejercicios * 0.20

if P_Tareas + P_Examenes + P_Ejercicios >= 70:
    print("El alumno esta Aprobado")
else:
    print("No aprobado, requiere una segunda oportunidad")

print("Ejercicio 3")

peso = float(input("Ingresa el peso del paquete (kg): "))
distancia = float(input("Ingresa la distancia que recorrera el paquete (km): "))
fragilidad = str(input("Ingresa la fragilidad 'SI' o 'NO': "))

if peso <= 5:
    Costo_Peso = 50
else:
    Costo_Peso = 200

if distancia <= 50:
    Costo_Distancia = 30
else:
    Costo_Distancia = 70

if fragilidad == "SI":
    Costo_Fragilidad = 100
else:
    Costo_Fragilidad = 50

Subtotal = Costo_Distancia + Costo_Fragilidad + Costo_Peso
Costo_Total = (Subtotal)*1.16

print(f"El subtotal del envio seria: ${Subtotal:.2f}"  )
print(f"IVA : 16%" )
print(f"El Costo total del envio seria: ${Costo_Total:.2f}" )
'''
Calcula el subtotal del envío
Calcula el IVA: 16% sobre el subtotal
Muestra el desglose subtotal, IVA y total con 2 decimales'''

