'''Mis  Tareas

***************
1. Agregar tarea
2. Eliminar tarea
3. Ver tareas
4. Marcar tarea como completada
5. Buscar tarea
6. Salir

Si elige agregar  tarea
Debe pedir el nombre de la tarea y agregarla a la lista
Eliminar una tarea
Debe permitir ingresar el nombre de la tarea a eliminar
Si la tarea existe, debe eliminarla de la lista.
Ver las tareas,
Debe mostrar todas las tareas en la lista.
Marcar una tarea como completada
Ingresar el nombre de la tarea y el programa debe agregar "Completada" al nombre de la tarea.
Buscar una tarea
Preguntar el nombre de la tarea y buscarla en la lista, y decir si existe o no.'''



eleccion = 0

lista1 = []
while eleccion != 6:
    print('''Hola Bienvenido al administrador de tareas!
    Elige la opcion que quieras:
    1. Agregar tarea
    2. Eliminar tarea
    3. Ver tareas
    4. Marcar tarea como completada
    5. Buscar tarea
    6. Salir''')

    eleccion = int(input("Ingrese la opcion que desee: "))
    if eleccion == 1:
        agregartarea = str(input("Ingrese el nombre de la tarea que desee agregar: "))
        lista1.insert(0, agregartarea)

    if eleccion == 2:
        eleminiartarea = str(input(f'''Escriba el nombre de la tarea que desea eliminar: '''))
        if eleminiartarea in lista1:
            del lista1[lista1.index(eleminiartarea)]
            print(f"La tarea {eleminiartarea} ha sido eliminada exitosamente")
        else:
            print("Tarea no encontrada")

    if eleccion == 3:
        print("Tareas:", lista1)

    if eleccion == 4:
        tareacompletada = str(input("Ingrese el nombre de la tarea que desea marcar completada: "))
        if tareacompletada in lista1:
            indice1 = lista1.index(tareacompletada)
            lista1[indice1] = tareacompletada + "(Completada)"
            print(f"Tarea {tareacompletada} marcada como completada exitosamente")
        else:
            print("Tarea no encontrada")

    if eleccion == 5:
        buscartarea = str(input("Ingrese la tarea que desea buscar: "))
        if buscartarea in lista1:
            print("La tarea si esta en la lista")
        else:
            print("Tarea no encontrada")

    if eleccion == 6:
        print("Gracias por usar el servicio, se le hara un pagare por 5000 pesos. Hasta luego")


