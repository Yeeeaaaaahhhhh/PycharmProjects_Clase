import tkinter as tk
from tkinter import ttk
import sqlite3

conex = sqlite3.connect("Actividad 14.3.db")
cursor = conex.cursor()
def crear_tabla():
    cursor.execute("""CREATE TABLE IF NOT EXISTS alumnos   (
        ID TEXT PRIMARY KEY,
        nombre TEXT NOT NULL,
        promedio TEXT NOT NULL,
        carrera TEXT NOT NULL
        )
    """)
    conex.commit()

    print("Base de datos y tablas creadas (si no existian)")

#ventana Principal
ventana = tk.Tk()
ventana.title("Formulario de alumnos")
ventana.geometry("600x500")

#Titulo
titulo = ttk.Label(ventana, text="Formulario de alumnos",
font=("Helvetica", 20, "bold"))
titulo.pack(pady=50)

#label y campo para el nombre
label_id = tk.Label(ventana, text="ID del alumno",)
label_id.pack(pady=5)
entry_id = tk.Entry(ventana)
entry_id.pack(pady=5)

#label y campo para el nombre
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.pack(pady=5)
entry_nombre = tk.Entry(ventana,width=50)
entry_nombre.pack(pady=5)

#label y campos promedio
label_promedio = tk.Label(ventana, text="Promedio:")
label_promedio.pack(pady=5)
entry_promedio = tk.Entry(ventana,width=50)
entry_promedio.pack(pady=5)

#label y combo box
label_carrera = tk.Label(ventana, text="Carrera:")
label_carrera.pack(pady=5)
combo_carrera = ttk.Combobox(ventana, width=15, values=["TI"," Quimica", "Mecatronica"])
combo_carrera.pack(pady=5)

#enviar datos
def enviar_datos():
    ID = entry_nombre.get()
    nombre = entry_nombre.get()
    promedio = entry_promedio.get()
    carrera = combo_carrera.get()
    print(f"Nombre :{nombre} - Promedio :{promedio} - Carera :{carrera}")

    try:
        cursor.execute("""
            INSERT INTO alumnos (ID, nombre, promedio, carrera)
            VALUES (?, ?, ?, ?)
        """, (ID, nombre, promedio, carrera))
        conex.commit()

        print("Alumno dado de alta correctamente")
    except sqlite3.IntegrityError:
        print("Esa matricula ya esta registrada")

    alumnos = cursor.fetchall()
    print("Lista de empleados")
    for ID, nombre, promedio, carrera in alumnos:
        print(f"Clave: {ID} | Nombre: {nombre} | Puesto: {promedio}  | Salario:{carrera}")
    conex.commit()

boton_enviar = ttk.Button(ventana, text="Enviar datos", command=enviar_datos)
boton_enviar.pack(pady=20)

def limpiar_datos():
    entry_nombre.delete(0, tk.END)
    entry_promedio.delete(0, tk.END)
    combo_carrera.set('')

boton_nuevo = tk.Button(ventana, text="Nuevo", command=limpiar_datos)
boton_nuevo.pack(pady=10)

crear_tabla()
ventana.mainloop()

