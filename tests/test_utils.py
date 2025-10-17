# tests/test_utils.py
import os
import shutil
import pytest
import tempfile
from utils import obtener_extension, crear_carpeta, mover_archivo

# Fixture para crear un directorio temporal para pruebas
@pytest.fixture
def temp_dir():
    """Crea un directorio temporal para pruebas y lo elimina después."""
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir, ignore_errors=True)

def test_obtener_extension():
    """Prueba la función obtener_extension."""
    assert obtener_extension("documento.pdf") == ".pdf"
    assert obtener_extension("foto.PNG") == ".png"
    assert obtener_extension("sin_extension") == ""
    assert obtener_extension(".gitignore") == ""

def test_crear_carpeta(temp_dir):
    """Prueba la función crear_carpeta."""
    nueva_carpeta = os.path.join(temp_dir, "Documentos")
    
    # Caso normal: Crear carpeta
    crear_carpeta(nueva_carpeta)
    assert os.path.exists(nueva_carpeta)
    
    # Caso dry-run: No crea la carpeta
    crear_carpeta(nueva_carpeta, dry_run=True)
    assert os.path.exists(nueva_carpeta)  # No debería crear otra carpeta
    
    # Caso verbose: Verifica que no falle
    crear_carpeta(nueva_carpeta, verbose=True)
    assert os.path.exists(nueva_carpeta)

def test_mover_archivo(temp_dir):
    """Prueba la función mover_archivo."""
    # Crear un archivo de prueba
    archivo_origen = os.path.join(temp_dir, "test.txt")
    with open(archivo_origen, "w") as f:
        f.write("Contenido de prueba")
    
    destino_carpeta = os.path.join(temp_dir, "Destino")
    destino_completo = os.path.join(destino_carpeta, "test.txt")
    
    # Caso normal: Mover archivo
    crear_carpeta(destino_carpeta)
    mover_archivo(archivo_origen, destino_carpeta, "test.txt")
    assert os.path.exists(destino_completo)
    assert not os.path.exists(archivo_origen)
    
    # Caso dry-run: No mueve el archivo
    archivo_origen = os.path.join(temp_dir, "test2.txt")
    with open(archivo_origen, "w") as f:
        f.write("Contenido de prueba")
    mover_archivo(archivo_origen, destino_carpeta, "test2.txt", dry_run=True)
    assert os.path.exists(archivo_origen)
    assert not os.path.exists(os.path.join(destino_carpeta, "test2.txt"))
    
    # Caso duplicado: Renombra el archivo
    archivo_origen = os.path.join(temp_dir, "test3.txt")
    with open(archivo_origen, "w") as f:
        f.write("Contenido de prueba")
    with open(destino_completo, "w") as f:  # Crear archivo con el mismo nombre
        f.write("Contenido existente")
    mover_archivo(archivo_origen, destino_carpeta, "test.txt")
    assert os.path.exists(os.path.join(destino_carpeta, "test_1.txt"))
    assert not os.path.exists(archivo_origen)

def test_mover_archivo_error(temp_dir):
    """Prueba mover_archivo con un error (ruta inválida)."""
    archivo_origen = os.path.join(temp_dir, "test.txt")
    with open(archivo_origen, "w") as f:
        f.write("Contenido de prueba")
    
    destino_invalido = "/ruta/invalida/no/existe"
    with pytest.raises(Exception):
        mover_archivo(archivo_origen, destino_invalido, "test.txt")