import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organizar_archivos(ruta_base):
    """Función para organizar los archivos por extensión"""
    archivos_carpetas = os.listdir(ruta_base)

    for archivo_carpeta in archivos_carpetas:
        ruta_inicial = os.path.join(ruta_base, archivo_carpeta)

        # Solo procesamos archivos (ignoramos carpetas)
        if os.path.isfile(ruta_inicial):
            # Separamos el nombre del archivo y la extensión
            nombre, extension = os.path.splitext(archivo_carpeta)
            extension = extension.lower().strip('.')  # Quitamos el punto y ponemos en minúsculas

            if extension:  # Aseguramos que haya extensión
                nombre_nueva_carpeta = f'Extension_{extension}'
                ruta_final = os.path.join(ruta_base, nombre_nueva_carpeta)

                # Si la carpeta no existe, la creamos
                if not os.path.exists(ruta_final):
                    os.makedirs(ruta_final)

                # Movemos el archivo a su carpeta
                shutil.move(ruta_inicial, os.path.join(ruta_final, archivo_carpeta))

    messagebox.showinfo("Éxito", "¡Archivos organizados con éxito!")

def seleccionar_carpeta():
    """Función para abrir el explorador de archivos y seleccionar la carpeta"""
    ruta = filedialog.askdirectory(title="Seleccionar carpeta a organizar")
    
    if ruta:
        organizar_archivos(ruta)

# Interfaz con Tkinter
ventana = tk.Tk()
ventana.title("Organizador de Archivos por Extensión")
ventana.geometry("400x180")
ventana.resizable(False, False)

etiqueta = tk.Label(ventana, text="Haz clic para seleccionar una carpeta a organizar:", font=("Arial", 12))
etiqueta.pack(pady=20)

boton = tk.Button(ventana, text="Seleccionar Carpeta", command=seleccionar_carpeta, font=("Arial", 12), bg="#4CAF50", fg="white")
boton.pack()

ventana.mainloop()
