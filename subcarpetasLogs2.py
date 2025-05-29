import os
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox

def organizar_archivos(ruta_base):
    """Función para organizar los archivos por extensión"""
    dir_ruta_base = os.listdir(ruta_base)

    for archivo_o_carpeta in dir_ruta_base:
        archivo_con_ruta_completa = os.path.join(ruta_base, archivo_o_carpeta)

        # Solo procesamos archivos (ignoramos carpetas)
        if os.path.isfile(archivo_con_ruta_completa):
            # Separamos el nombre del archivo y la extensión
            nombre, extension = os.path.splitext(archivo_o_carpeta)
            extension = extension.lower().strip('.')  # Quitamos el punto y ponemos en minúsculas

            # Nos aseguramos que exista EXTENSION:
            if extension:
                # Obtener la ultima fecha-modificacion:
                fecha_modif = datetime.fromtimestamp(os.path.getmtime(archivo_con_ruta_completa))
                subcarpeta_fecha = fecha_modif.strftime('%Y-%m')

                # Crear la subcarpeta si no existe:
                carpeta_tipo = os.path.join(ruta_base, extension)
                carpeta_fecha = os.path.join(carpeta_tipo, subcarpeta_fecha)

                # Si la carpeta no existe, la creamos
                if not os.path.exists(carpeta_fecha):
                    os.makedirs(carpeta_fecha)

                # Movemos el archivo a su carpeta
                ruta_final_total = os.path.join(carpeta_fecha, archivo_o_carpeta)
                shutil.move(archivo_con_ruta_completa, ruta_final_total)

                # Creamos archivo .log:
                with open(os.path.join(ruta_base, "logs_archivos_movidos.txt"), "a", encoding="utf-8") as log:
                    log.write(f"{datetime.now().strftime('%Y-%m-%d %H: %M: %S')} movido: {archivo_o_carpeta} --> {ruta_final_total}\n")

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
