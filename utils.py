# utils.py
import os
import shutil
import logging

# Configuración inicial de logging
logging.basicConfig(
    filename='logs/organizador.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def obtener_extension(archivo):
    """Devuelve la extensión de un archivo en minúsculas."""
    ext = os.path.splitext(archivo)[1].lower()
    logging.debug(f"Obtenida extensión '{ext}' para el archivo '{archivo}'")
    return ext

def crear_carpeta(ruta, dry_run=False, verbose=False):
    """Crea una carpeta si no existe, salvo en modo dry-run."""
    try:
        if not os.path.exists(ruta):
            if dry_run:
                logging.info(f"[DRY-RUN] Se habría creado la carpeta: {ruta}")
                if verbose:
                    print(f"[DRY-RUN] Se habría creado la carpeta: {ruta}")
            else:
                os.makedirs(ruta)
                logging.info(f"Carpeta creada: {ruta}")
                if verbose:
                    print(f"Carpeta creada: {ruta}")
    except Exception as e:
        logging.error(f"Error al crear carpeta {ruta}: {str(e)}")
        if verbose:
            print(f"Error al crear carpeta {ruta}: {str(e)}")
        raise

def mover_archivo(origen, destino, archivo, dry_run=False, verbose=False):
    """Mueve un archivo a la carpeta de destino, manejando duplicados."""
    destino_completo = os.path.join(destino, archivo)
    base, ext = os.path.splitext(archivo)
    contador = 1

    # Manejar archivos duplicados
    while os.path.exists(destino_completo):
        nuevo_nombre = f"{base}_{contador}{ext}"
        destino_completo = os.path.join(destino, nuevo_nombre)
        logging.warning(f"Nombre duplicado detectado, renombrando a: {nuevo_nombre}")
        if verbose:
            print(f"Nombre duplicado detectado, renombrando a: {nuevo_nombre}")
        contador += 1

    try:
        if dry_run:
            logging.info(f"[DRY-RUN] Se habría movido: {archivo} -> {destino_completo}")
            if verbose:
                print(f"[DRY-RUN] Se habría movido: {archivo} -> {destino_completo}")
        else:
            shutil.move(origen, destino_completo)
            logging.info(f"Archivo movido: {archivo} -> {destino_completo}")
            if verbose:
                print(f"Archivo movido: {archivo} -> {destino_completo}")
    except Exception as e:
        logging.error(f"Error al mover {archivo}: {str(e)}")
        if verbose:
            print(f"Error al mover {archivo}: {str(e)}")
        raise