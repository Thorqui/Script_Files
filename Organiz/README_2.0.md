### Versión 2.0: Organizador de Descargas con GUI

```markdown
# 🗂️ Organizador de Descargas con GUI (Versión 2.0)

Un script en Python con interfaz gráfica (Tkinter), convertido en ejecutable (`.exe`), que organiza automáticamente cualquier carpeta según el tipo de archivo. Incluye un registro de archivos movidos en `log_organizador.txt` para un seguimiento detallado.
```

## 📋 Descripción

Esta versión mejora el Organizador de Descargas con una interfaz gráfica amigable, permitiendo al usuario seleccionar una carpeta y organizarla con un solo clic. Los archivos se clasifican en subcarpetas (Imágenes, Documentos, Videos, Música, Otros), y cada operación se registra en un archivo de log.


## 🚀 Tecnologías Utilizadas

| Tecnología     | Descripción                     |
|----------------|---------------------------------|
| **Python 3.10+** | Lógica del script              |
| **Tkinter**    | Interfaz gráfica               |
| **PyInstaller**| Generación del ejecutable `.exe`|
| **os, shutil** | Manipulación de archivos       |


## 🧩 Características

- 🖼️ Interfaz gráfica con Tkinter para una experiencia de usuario sencilla.
- 📍 Selección de carpeta personalizada mediante un explorador de archivos.
- 📂 Organiza archivos por extensión:
  - **Imágenes**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`
  - **Documentos**: `.pdf`, `.docx`, `.doc`, `.txt`, `.xlsx`, `.pptx`, `.xls`, `.ppt`, `.csv`
  - **Videos**: `.mp4`, `.avi`, `.mov`, `.mkv`, `.wmv`
  - **Música**: `.mp3`, `.wav`, `.aac`, `.flac`
  - **Otros**: Cualquier otro archivo
- 📜 Registro de archivos movidos en `log_organizador.txt`.
- ✅ Ejecutable `.exe` para usar con doble clic, sin necesidad de Python.
- 🚫 Evita sobrescritura renombrando archivos duplicados.


## ⚙️ Cómo Usar

### Código Fuente
1. **Requisitos**:
   - Python 3.10+ (incluye Tkinter por defecto).
2. **Clona el repositorio**:
   ```bash
   git clone https://github.com/Thorqui/Organizador-Descargas.git
   cd Organizador-Descargas/v2.0
   ```

Ejecuta el script:
```bash
python organizador_gui.py
```

Uso:
Se abrirá una ventana gráfica.  
Haz clic en el botón para seleccionar una carpeta.  
Presiona “Organizar” para clasificar los archivos.   
Revisa la carpeta seleccionada y el archivo log_organizador.txt para el registro.  

Ejecutable

Requisitos: Windows (o compatible con el .exe).  
Uso:

Descarga v2.0/organizador_gui.exe desde el repositorio.  
Haz doble clic para abrir la interfaz gráfica.  
Selecciona una carpeta y haz clic en “Organizar”.  
Nota: El .exe no admite argumentos CLI; usa la interfaz para configuraciones.  


Generar el .exe:

Instala PyInstaller:
```bash
pip install pyinstaller
```

Genera el ejecutable:
```bash
pyinstaller --onefile --windowed organizador_gui.py
```

Encuentra el .exe en la carpeta dist/.



## 🧠 Mejoras Futuras

🔍 Añadir un visor de logs en la interfaz gráfica.  
🗂️ Subclasificación para la carpeta "Otros".   
⚙️ Opciones avanzadas en la GUI (ej., excluir ciertos tipos de archivos).   
⏰ Programación automática para organizar carpetas periódicamente.   


## 👨‍💻 Autor
Aitor Quilez Herrero (Thorqui)  
🔗 GitHub - Thorqui

## 💡 Notas Adicionales

- El código fuente es completamente funcional y no requiere el .exe.
- El archivo log_organizador.txt se genera en la carpeta donde se ejecuta el .exe o script.
- Reporta problemas en: 🌐 https://github.com/Thorqui/Organizador-Descargas.
