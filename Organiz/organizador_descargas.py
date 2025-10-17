import os
import shutil

# Carpeta de descargas (cámbiala si tu ruta es distinta)
DESCARGAS = os.path.join(os.path.expanduser("~"), "Downloads")

# Mapeo de carpetas por tipo de archivo
EXTENSIONES = {
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Musica": [".mp3", ".wav", ".aac"],
}

# Carpeta por defecto para archivos que no coincidan
OTROS = "Otros"

def organizar_descargas():
    for archivo in os.listdir(DESCARGAS):
        ruta_completa = os.path.join(DESCARGAS, archivo)
        if os.path.isfile(ruta_completa):
            movido = False
            # Revisar cada categoría
            for carpeta, extensiones in EXTENSIONES.items():
                if any(archivo.lower().endswith(ext) for ext in extensiones):
                    destino = os.path.join(DESCARGAS, carpeta)
                    os.makedirs(destino, exist_ok=True)
                    shutil.move(ruta_completa, os.path.join(destino, archivo))
                    movido = True
                    break
            # Archivos que no coinciden
            if not movido:
                destino = os.path.join(DESCARGAS, OTROS)
                os.makedirs(destino, exist_ok=True)
                shutil.move(ruta_completa, os.path.join(destino, archivo))

    print("¡Organización completada! ✅")

if __name__ == "__main__":
    organizar_descargas()
