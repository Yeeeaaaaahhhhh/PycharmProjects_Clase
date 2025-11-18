'''#Escenario: Trabajas en una empresa donde los vendedores reciben
# 23% de comisión sobre sus ventas mensuales.
#Pide el nombre del vendedor.
Pide el monto total vendido en el mes (número decimal).
Calcula la comisión
Muestra una frase completa que incluya el nombre y el monto de comisión
 (con 2 decimales).
Sugerencia de impresión con 2 decimales: print(f"Comisión: ${comision:.2f}")'''

print("Ejercicio 2")

nombre = input('Escribe tu nombre, estimado vendedor ')
monto =  float(input('Escribe el monto total vendido del mes, estimado vendedor '))
comision = monto * 1.23
print(f"La comision total del monto dado es: ${comision:.2f}")

print("Ejercicio 3")

'''Área de un triángulo
Pide base y altura (números decimales).
Calcula el área con la fórmula: area = (base * altura) / 2.
Muestra los tres valores: base, altura y área (con 2 decimales para el área).'''

print('Vamos a calcular el area de un triangulo!')
base = float(input('escribe la longitud de la base de tu triangulo '))
altura = float(input('escribe la altura de tu triangulo '))
area = (base * altura)/2
print(f"El area del triangulo es: {area:.2f}")

