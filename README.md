### README Dual - Versión 1.0 y Versión 2.0

```markdown
# 🗂️ Organizador de Descargas: Versión 1.0 & Versión 2.0

Este repositorio contiene dos versiones de una herramienta en Python para organizar automáticamente archivos según su tipo. Cada versión incluye un ejecutable (`.exe`) para facilitar su uso en Windows sin necesidad de configuraciones complejas.

- **Versión 1.0**: Un script CLI (línea de comandos) que organiza la carpeta de descargas con opciones avanzadas como `--verbose` y `--list-others`.
- **Versión 2.0**: Una versión mejorada con interfaz gráfica (Tkinter), selección de carpeta, y registro en `log_organizador.txt`.

Ambas versiones son ideales para mantener tus archivos organizados, con enfoques diferentes: la versión 1.0 para usuarios que prefieren la terminal, y la versión 2.0 para quienes buscan una experiencia visual.


## 📋 Descripción

### Versión 1.0: Organizador de Descargas (CLI)
Un script en Python que clasifica archivos en la carpeta de descargas (o una carpeta especificada) en subcarpetas según su extensión: Imágenes, Documentos, Videos, Música, y Otros. Incluye un ejecutable para usarlo con doble clic y opciones CLI para personalización.

### Versión 2.0: Organizador de Descargas con GUI
Una evolución del script con una interfaz gráfica en Tkinter. Permite seleccionar una carpeta mediante un explorador de archivos, organiza los archivos en las mismas categorías, y genera un registro en `log_organizador.txt`. El ejecutable es ideal para usuarios no técnicos.

---

## 🛠️ Tecnologías Utilizadas

| Proyecto                | Tecnologías                          | Descripción                              |
|-------------------------|--------------------------------------|------------------------------------------|
| Versión 1.0 (CLI)       | Python 3.10+, colorama, PyInstaller  | Script CLI y ejecutable                  |
| Versión 2.0 (GUI)       | Python 3.10+, Tkinter, PyInstaller   | Interfaz gráfica y ejecutable            |

---

## 📂 Estructura del Repositorio

```plaintext
Organizador-Descargas/
├── v1.0/
│   ├── organizador_descargas.py # Código fuente (CLI)
│   └── organizador_descargas.exe # Ejecutable para Windows
├── v2.0/
│   ├── organizador_gui.py        # Código fuente (GUI)
│   └── organizador_gui.exe      # Ejecutable para Windows
├── README.md                    # Este archivo
```

🚀 Cómo Usar
Versión 1.0: Organizador de Descargas (CLI)
Código Fuente

Requisitos:

Python 3.10+.
Instala colorama:
```bash
pip install colorama
```


Clona el repositorio:
```bash
git clone https://github.com/Thorqui/Organizador-Descargas.git
cd Organizador-Descargas/v1.0
```
Ejecuta el script:

Por defecto, organiza ~/Downloads:
```bash
python organizador_descargas.py
```
Con opciones:
```bash
python organizador_descargas.py --folder ~/Descargas --verbose --list-others
```
Opciones:

--folder RUTA: Carpeta a organizar.  
--verbose: Detalles de cada archivo movido.  
--list-others: Listado de archivos en "Otros" (nombre y tamaño).  




Salida:

Archivos organizados en Imágenes, Documentos, Videos, Música, Otros   
Ejemplo:  
textMovido: foto.jpg -> Imágenes/foto.jpg  
--- Resumen de organización (2025-10-17 09:07:23) ---  
Imágenes: 1 archivo(s)  
Otros: 1 archivo(s)  
--- Detalles de archivos en 'Otros' ---  
random.xyz: 0.50 MB  
¡Organización completada! ✅  




Executable

Requisitos: Windows.
Uso:

Descarga v1.0/organizador_descargas.exe.  
Haz doble clic para organizar ~/Downloads.  
Para opciones, usa una terminal:  
```bash
v1.0\organizador_descargas.exe --folder "C:\Users\TuUsuario\Descargas" --verbose --list-others
```
Nota: Si el .exe no admite argumentos, usa el código fuente.


Generar el .exe:
```bash
pip install pyinstaller
pyinstaller --onefile organizador_descargas.py
```

Características

📂 Clasificación por extensión.  
🚫 Evita sobrescritura.  
🔔 Resumen con colores.  
📋 Listado de "Otros" (--list-others).  
🔧 Opciones CLI.  
✅ Ejecutable sin Python.  


Versión 2.0: Organizador de Descargas con GUI
Código Fuente

Requisitos:

Python 3.10+ (incluye Tkinter).


Clona el repositorio:
```bash
git clone https://github.com/Thorqui/Organizador-Descargas.git
cd Organizador-Descargas/v2.0
```
Ejecuta el script:
```bash
python organizador_gui.py
```
Uso:

Abre la ventana gráfica.  
Selecciona una carpeta.  
Haz clic en “Organizar”.  
Revisa la carpeta y log_organizador.txt.  
 


Ejecutable

Requisitos: Windows.
Uso:

Descarga v2.0/organizador_gui.exe.     
Haz doble clic para abrir la interfaz.     
Selecciona una carpeta y haz clic en “Organizar”.   


Generar el .exe:   
```bash
pip install pyinstaller   
pyinstaller --onefile --windowed organizador_gui.py  
```

Características

🖼️ Interfaz gráfica con Tkinter.   
📍 Selección de carpeta.   
📂 Clasificación por extensión.   
📜 Registro en log_organizador.txt.   
✅ Ejecutable sin Python.   
🚫 Evita sobrescritura.   


## 🛠️ Instalación

Clona el repositorio:
```bash
git clone https://github.com/Thorqui/Organizador-Descargas.git
cd Organizador-Descargas
```
Versión 1.0 (CLI):

Instala Python 3.10+.
Instala colorama:
```bash
pip install colorama
```
Usa v1.0/organizador_descargas.py o el .exe.


Versión 2.0 (GUI):

Instala Python 3.10+ (Tkinter incluido).  
Usa v2.0/organizador_gui.py o el .exe.




## 🎮 Notas sobre los Ejecutables

organizador_descargas.exe (v1.0): Puede no admitir argumentos CLI; usa el código fuente para opciones avanzadas.  
organizador_gui.exe (v2.0): Ejecuta la interfaz gráfica; configuraciones solo a través de la GUI.  
Compatibilidad: Diseñados para Windows. Para macOS/Linux, usa el código fuente o genera nuevos ejecutables.  


## 📝 Planes Futuros
Versión 1.0

🖼️ Añadir interfaz gráfica (como en v2.0).  
📜 Registro en log.txt.  
⏰ Programación automática.  
📋 Subclasificación para "Otros".  

Versión 2.0

🔍 Visor de logs en la GUI.  
🗂️ Subclasificación para "Otros".  
⚙️ Opciones avanzadas en la GUI.  
⏰ Programación periódica.  
  

## 👨‍💻 Autor
Aitor Quilez Herrero (Thorqui)  
🔗 GitHub - Thorqui

## 💡 Notas Adicionales

- Los códigos fuente son funcionales y no requieren los .exe.
- Los .exe facilitan el uso en Windows, pero pueden tener limitaciones.
- Reporta problemas en: 🌐 https://github.com/Thorqui/Organizador-Descargas.
- Ambas versiones son complementarias: usa v1.0 para automatización en terminal, y v2.0 para una experiencia visual.
