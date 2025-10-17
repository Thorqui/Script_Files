# 🗂️ Organizador de Descargas con GUI

Proyecto en Python que organiza automáticamente cualquier carpeta según el tipo de archivo.  
Cuenta con **interfaz gráfica** y **registro de archivos movidos**.

---

## 🚀 Características

- Interfaz gráfica con **Tkinter**  
- Carpeta seleccionable por el usuario  
- Organización por tipo de archivo:
  - Imagenes, Documentos, Videos, Musica, Otros  
- Registro en `log_organizador.txt` con todos los archivos movidos  
- Ejecutable `.exe` listo para usar (no requiere Python)

---

## ⚙️ Uso

1️⃣ Ejecutar el archivo `organizador_gui.exe`  
2️⃣ Seleccionar la carpeta a organizar  
3️⃣ Presionar “Organizar”  
4️⃣ ¡Listo! Archivos movidos y log generado

---

## 🏗️ Cómo generar el .exe

```bash
pip install pyinstaller
pyinstaller --onefile --windowed organizador_gui.py

👨‍💻 Autor

Aitor (Thorqui)
🔗 GitHub – Thorqui