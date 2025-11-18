import sqlite3

conex = sqlite3.connect("ejemplo.db")

cursor = conex.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS productos (
        clave TEXT PRIMARY KEY,
        nombre TEXT NOT NULL,
        precio TEXT NOT NULL
        )
""")
print("Base de datos y tablas creadas (si no existian)")

productos = [
    ("P001", "Lapiz 0", "500"),
    ("P002", "Compu", "15000"),
    ("P003", "Mochila", "1000"),
]

for producto in productos:
    cursor.execute("""
    INSERT INTO productos (clave, nombre, precio)
    VALUES (?, ?, ?)
    """, producto)

cursor.execute("SELECT * FROM productos")
registros = cursor.fetchall()
print("Lista de registros")
for clave, nombre, precio in registros:
    print(f"Clave: {clave} | Nombre: {nombre} | Precio: {precio}")

conex.commit()
conex.close()
