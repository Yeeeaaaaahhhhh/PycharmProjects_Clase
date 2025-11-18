import sqlite3

conex = sqlite3.connect("Actividad 14.2.db")
cursor = conex.cursor()


def crear_tabla():
    cursor.execute("""CREATE TABLE IF NOT EXISTS empleados   (
        clave TEXT PRIMARY KEY,
        nombre TEXT NOT NULL,
        puesto TEXT NOT NULL,
        salario TEXT NOT NULL
        )
    """)
    conex.commit()

    print("Base de datos y tablas creadas (si no existian)")


def alta_alumno():
    clave = input("Ingresa la clave: ")
    nombre = input("Ingresa el nombre: ")
    puesto = input("Ingresa el puesto: ")
    salario = input("Ingresa el salario: ")
    try:
        cursor.execute("""
            INSERT INTO empleados (clave, nombre, puesto, salario)
            VALUES (?, ?, ?, ?)
        """, (clave, nombre, puesto, salario))
        conex.commit()

        print("Alumno dado de alta correctamente")
    except sqlite3.IntegrityError:
        print("Esa matricula ya esta registrada")



def consultar_alumno():
    clave = input("Ingresa clave para buscar: ")
    cursor.execute("SELECT * FROM empleados WHERE clave = ?", (clave,))
    empleado = cursor.fetchone()
    if empleado:
        print(f"Empleado encontrado: clave {empleado[0]}, nombre {empleado[1]}, puesto [{empleado[2]}, salario {empleado[3]}]")
    else:
        print("Empleado no encontrado")

def eliminar_alumno():
    matricula = input("Ingrese clave a elminar")
    cursor.execute("DELETE FROM empleados WHERE clave = ?", (matricula,))
    if cursor.rowcount > 0:
        conex.commit()
        print("Eliminado correctamente")
    else:
        print("Empleado no encontrado")
def imprimir_tabla():
    cursor.execute("SELECT * FROM empleados")
    registros = cursor.fetchall()
    print("Lista de empleados")
    for clave, nombre, puesto, salario in registros:
        print(f"Clave: {clave} | Nombre: {nombre} | Puesto: {puesto}  | Salario: {salario}")
    conex.commit()

opcion = 0
while opcion != 6:
    print(''' ----- Menu -----
1. Crear base de datos
2. Dar de alta a un alumno
3. Consultar toda la tabla
4. Consultar alumno por matricula
5. Eliminar a un alumno
6. Salir''')

    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        crear_tabla()
    if opcion == 2:
        alta_alumno()
    if opcion == 3:
        imprimir_tabla()
    if opcion == 4:
        consultar_alumno()
    if opcion == 5:
        eliminar_alumno()
    if opcion == 6:
        print("Saliendo...")
    else:
        print("Opcion invalida")
conex.close()