import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Diccionario de extensiones --> carpetas correspondientes
dict_ext_carpetas = {
    ".txt": "Texto",
    ".asm": "Ensamblador_Z80",
    ".zip": "Zip",
    ".png": "Imagen",
    ".jpg": "Imagen"
}

def crear_carpetas_si_no_existen(base_path):
    """Crea las carpetas según el diccionario, si no existen"""
    for carpeta in set(dict_ext_carpetas.values()):
        ruta_carpeta = os.path.join(base_path, carpeta)
        if not os.path.exists(ruta_carpeta):
            os.makedirs(ruta_carpeta)

def organizar_archivos(base_path):
    """Organiza los archivos en carpetas según su extensión"""
    archivos = os.listdir(base_path)

    for archivo in archivos:
        ruta_inicial = os.path.join(base_path, archivo)
        if os.path.isfile(ruta_inicial):
            _, extension = os.path.splitext(archivo)
            extension = extension.lower()
            if extension in dict_ext_carpetas:
                carpeta_destino = dict_ext_carpetas[extension]
                ruta_destino = os.path.join(base_path, carpeta_destino, archivo)
                shutil.move(ruta_inicial, ruta_destino)

    messagebox.showinfo("Éxito", "¡Archivos organizados con éxito!")

def seleccionar_carpeta():
    ruta = filedialog.askdirectory(title="Seleccionar carpeta a organizar")
    if ruta:
        crear_carpetas_si_no_existen(ruta)
        organizar_archivos(ruta)

# Interfaz con Tkinter
ventana = tk.Tk()
ventana.title("Organizador de Archivos por Extensión")
ventana.geometry("400x150")
ventana.resizable(False, False)

etiqueta = tk.Label(ventana, text="Haz clic para seleccionar una carpeta a organizar:", font=("Arial", 12))
etiqueta.pack(pady=20)

boton = tk.Button(ventana, text="Seleccionar Carpeta", command=seleccionar_carpeta, font=("Arial", 12), bg="#4CAF50", fg="white")
boton.pack()

ventana.mainloop()
