import os
import shutil

# Carpeta base: donde está este script
CARPETA_BASE = os.path.dirname(os.path.abspath(__file__))

# Archivos o carpetas a borrar (puedes modificar esta lista)
objetivos = [
    "build",
    "__pycache__",
    ".pytest_cache",
    "dist",  # ❗ Elimina esto solo si quieres borrar también los .exe generados
]

# Opcional: eliminar archivos .spec generados por PyInstaller
for archivo in os.listdir(CARPETA_BASE):
    if archivo.endswith(".spec"):
        ruta_archivo = os.path.join(CARPETA_BASE, archivo)
        print(f"Eliminando archivo: {ruta_archivo}")
        os.remove(ruta_archivo)

# Eliminar carpetas especificadas
for objetivo in objetivos:
    ruta_objetivo = os.path.join(CARPETA_BASE, objetivo)
    if os.path.exists(ruta_objetivo):
        if os.path.isdir(ruta_objetivo):
            print(f"Eliminando carpeta: {ruta_objetivo}")
            shutil.rmtree(ruta_objetivo)
        else:
            print(f"Eliminando archivo: {ruta_objetivo}")
            os.remove(ruta_objetivo)

print("\n✅ Limpieza completada.")
