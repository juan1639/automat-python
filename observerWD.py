import os
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

ruta_base = r'C:\Users\User\Desktop\ZX Spectrum\asmJon - copia'

class ManejadorEventos(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"Nuevo archivo detectado: {event.src_path}")
            organizar_archivos(ruta_base)

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

organizar_archivos(ruta_base)

manejador_eventos = ManejadorEventos()
observador = Observer()
# recursive=False --> SOLO CARPETA ... si True --> Carpeta y subcarpetas:
observador.schedule(manejador_eventos, ruta_base, recursive=False)
observador.start()

print(f"Observer en carpeta: {ruta_base}")
print("CTRL + C --> Detener")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print('detenido program (observer)')
    observador.stop()

observador.join()
