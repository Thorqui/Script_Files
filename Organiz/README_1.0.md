# 🗂️ Organizador de Descargas (Versión 1.0)

Un script práctico en Python, convertido en ejecutable (`.exe`), que organiza automáticamente tu carpeta de descargas según el tipo de archivo. Ideal para mantener tu escritorio y descargas siempre ordenadas.


## 📋 Descripción

Este script clasifica los archivos en la carpeta de descargas (o una carpeta especificada) en subcarpetas según su extensión: Imágenes, Documentos, Videos, Música, y Otros. El ejecutable permite usarlo con un simple doble clic, sin necesidad de abrir Python o una terminal.


## 🚀 Tecnologías Utilizadas

| Tecnología     | Descripción                     |
|----------------|---------------------------------|
| **Python 3.10+** | Lógica del script              |
| **colorama**   | Colores en la consola          |
| **PyInstaller**| Generación del ejecutable `.exe`|
| **os, shutil** | Manipulación de archivos       |


## 🧩 Características

- 📂 Organiza archivos en carpetas según su extensión:
  - **Imágenes**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`
  - **Documentos**: `.pdf`, `.docx`, `.doc`, `.txt`, `.xlsx`, `.pptx`, `.xls`, `.ppt`, `.csv`
  - **Videos**: `.mp4`, `.avi`, `.mov`, `.mkv`, `.wmv`
  - **Música**: `.mp3`, `.wav`, `.aac`, `.flac`
  - **Archivos**: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`
  - **Otros**: Cualquier otro archivo
- 🚫 Evita sobrescritura renombrando archivos duplicados (ej., `archivo_1.jpg`).
- 🔔 Resumen detallado con colores y fecha/hora.
- 📋 Listado de archivos en "Otros" con tamaño (opción `--list-others`).
- 🔧 Opciones CLI: `--folder`, `--verbose`, `--list-others`.
- ✅ Ejecutable `.exe` para usar con doble clic.
- 🚀 No requiere abrir Python ni terminal.


## ⚙️ Cómo Usar

### Código Fuente
1. **Requisitos**:
   - Python 3.10+.
   - Instala `colorama`:
     ```bash
     pip install colorama
     ```

2. **Clona el repositorio:**
   ```bash
git clone https://github.com/Thorqui/Organizador-Descargas.git
cd Organizador-Descargas/v1.0
  ```

3. **Ejecuta el script:**

Por defecto, organiza ~/Downloads:
```bash
python organizador_descargas.py
```

Con opciones:
```bash
python organizador_descargas.py --folder ~/Descargas --verbose --list-others
```

Opciones disponibles:

--folder RUTA: Especifica la carpeta a organizar.
--verbose: Muestra detalles de cada archivo movido.
--list-others: Muestra un listado de archivos en "Otros" (nombre y tamaño).




Salida:

- Los archivos se mueven a carpetas correspondientes.
- Ejemplo con --verbose --list-others:
  
    Movido: foto.jpg -> Imágenes/foto.jpg  
    Movido a Otros: random.xyz -> Otros/random.xyz  
--- Resumen de organización (2025-10-17 09:07:23) ---  
    Imágenes: 1 archivo(s)  
    Otros: 1 archivo(s)  
--- Detalles de archivos en 'Otros' ---  
    random.xyz: 0.50 MB  
    ¡Organización completada! ✅  




Ejecutable

1. Requisitos: Windows (o compatible con el .exe).
2. Uso:

Descarga v1.0/organizador_descargas.exe desde el repositorio.  
Haz doble clic para organizar ~/Downloads.  
Para opciones avanzadas, abre una terminal:  

```bash
v1.0\organizador_descargas.exe --folder "C:\Users\TuUsuario\Descargas" --verbose --list-others
```
Nota: Algunos .exe no admiten argumentos CLI. Si falla, usa el código fuente.

3. Generar el .exe:

Instala PyInstaller:
```bash
pip install pyinstaller
```

Genera el ejecutable:
```bash
pyinstaller --onefile organizador_descargas.py
```

Encuentra el .exe en la carpeta dist/.


## 🧠 Mejoras Futuras

🖼️ Añadir interfaz gráfica con Tkinter (como en la versión 2.0).  
📍 Configuración de carpeta personalizada desde un archivo de configuración.   
📜 Registro de archivos movidos en un log.txt.  
⏰ Programación automática al iniciar sesión en Windows.  
📋 Subclasificación para la carpeta "Otros".  


## 👨‍💻 Autor
Aitor Quilez Herrero (Thorqui)
🔗 GitHub - Thorqui

## 💡 Notas Adicionales

- El código fuente es completamente funcional y no requiere el .exe.
- Reporta problemas en: 🌐 https://github.com/Thorqui/Organizador-Descargas.

