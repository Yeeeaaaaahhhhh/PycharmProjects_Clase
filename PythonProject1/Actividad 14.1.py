import sqlite3

conex = sqlite3.connect("Actividad 14.1.db")
cursor = conex.cursor()
def crear_tabla():

    cursor.execute("""CREATE TABLE IF NOT EXISTS empleados (
        clave TEXT PRIMARY KEY,
        nombre TEXT NOT NULL,
        puesto TEXT NOT NULL,
        salario TEXT NOT NULL
        )
    """)

    print("Base de datos y tablas creadas (si no existian)")
def insertar_datos():
    empleados = [
        ("1", "Juan Perez","Gerente", "1000000000"),
        ("2", "Ana Gomez","Secretaria" ,"300000"),
        ("3", "Carlos Lopez", "Programador" ,"10"),
        ("4", "Pablo Barriga", "Mascota" ,"1000000000000000"),
        ("5", "Luis Campos", "Limpieza" ,"1"),
    ]

    for empleado in empleados:
        cursor.execute("""
        INSERT INTO empleados (clave, nombre, puesto, salario)
        VALUES (?, ?, ?, ?)
        """,(clave, nombre, puesto, salario))

def imprimir_tabla():
    cursor.execute("SELECT * FROM empleados")
    registros = cursor.fetchall()
    print("Lista de empleados")
    for clave, nombre, puesto, salario in registros:
        print(f"Clave: {clave} | Nombre: {nombre} | Puesto: {puesto}  | Salario: {salario}")

conex.commit()
conex.close()

tabla = crear_tabla()
imprimir = imprimir_tabla()