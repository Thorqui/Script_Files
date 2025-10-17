# organizador.py
import os
import argparse
import logging
from tqdm import tqdm
from config import CATEGORIAS
from utils import obtener_extension, crear_carpeta, mover_archivo

# Configuración de logging
logging.basicConfig(
    filename='logs/organizador.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def organizar_carpeta(ruta, dry_run=False, verbose=False):
    """Organiza archivos en la ruta especificada según su extensión."""
    if not os.path.exists(ruta):
        logging.error(f"La ruta {ruta} no existe")
        print(f"Error: La ruta {ruta} no existe")
        return

    # Obtener lista de archivos para la barra de progreso
    archivos = [f for f in os.listdir(ruta) if os.path.isfile(os.path.join(ruta, f)) and f != os.path.basename(__file__)]
    
    try:
        for archivo in tqdm(archivos, desc="Organizando archivos", disable=not verbose):
            ruta_completa = os.path.join(ruta, archivo)
            
            # Solo procesar archivos, no directorios ni el propio script
            if os.path.isfile(ruta_completa):
                extension = obtener_extension(archivo)
                carpeta_destino = None
                
                # Buscar la categoría adecuada
                for categoria, extensiones in CATEGORIAS.items():
                    if extension in extensiones:
                        carpeta_destino = categoria
                        break
                
                # Si no hay categoría, usar "Otros"
                if not carpeta_destino:
                    carpeta_destino = "Otros"
                
                # Crear carpeta destino y mover archivo
                destino = os.path.join(ruta, carpeta_destino)
                try:
                    crear_carpeta(destino, dry_run, verbose)
                    mover_archivo(ruta_completa, destino, archivo, dry_run, verbose)
                except Exception as e:
                    logging.error(f"No se pudo procesar {archivo}: {str(e)}")
                    if verbose:
                        print(f"No se pudo procesar {archivo}: {str(e)}")
    except Exception as e:
        logging.error(f"Error general al organizar la carpeta {ruta}: {str(e)}")
        if verbose:
            print(f"Error general al organizar la carpeta: {str(e)}")

def main():
    """Configura y ejecuta el organizador con argumentos de línea de comandos."""
    parser = argparse.ArgumentParser(
        description="Organizador Automático de Archivos: clasifica archivos por extensión en subcarpetas."
    )
    parser.add_argument(
        "--path",
        type=str,
        default=os.path.expanduser("~/Downloads"),
        help="Ruta de la carpeta a organizar (por defecto: carpeta Descargas)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simula la organización sin mover archivos"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Muestra información detallada en la consola"
    )
    
    args = parser.parse_args()
    
    if args.verbose:
        print(f"Organizando carpeta: {args.path}")
        if args.dry_run:
            print("Modo simulación activado: no se moverán archivos")
    
    organizar_carpeta(args.path, args.dry_run, args.verbose)
    
    if args.verbose or not args.dry_run:
        print("¡Organización completada! Revisa logs/organizador.log para detalles.")

if __name__ == "__main__":
    main()