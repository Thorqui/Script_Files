# config.py
import json
import os

def cargar_configuracion(ruta_config="config.json"):
    """Carga las categorías desde un archivo config.json."""
    try:
        if not os.path.exists(ruta_config):
            raise FileNotFoundError(f"El archivo {ruta_config} no existe")
        with open(ruta_config, 'r') as archivo:
            config = json.load(archivo)
        return config["categorias"]
    except Exception as e:
        print(f"Error al cargar configuración: {str(e)}")
        # Configuración por defecto si falla la carga
        return {
            "Documentos": [".pdf", ".docx", ".txt"],
            "Imágenes": [".jpg", ".jpeg", ".png", ".gif"],
            "Videos": [".mp4", ".mkv", ".avi"],
            "Música": [".mp3", ".wav", ".flac"],
            "Otros": []
        }

CATEGORIAS = cargar_configuracion()