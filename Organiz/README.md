# 🗂️ Organizador de Descargas

Un **script práctico en Python** convertido en **ejecutable** (`.exe`) que organiza automáticamente tu carpeta de descargas según el tipo de archivo.  

Ideal para mantener tu escritorio y descargas siempre ordenadas.

---

## 🚀 Tecnologías utilizadas

- Python 3.10+
- PyInstaller (para generar el `.exe`)
- Librerías estándar: `os`, `shutil`

---

## 🧩 Funcionalidades

- Organiza archivos en carpetas según su extensión:
  - **Imagenes:** `.jpg, .jpeg, .png, .gif, .bmp`
  - **Documentos:** `.pdf, .docx, .txt, .xlsx, .pptx`
  - **Videos:** `.mp4, .avi, .mov, .mkv`
  - **Musica:** `.mp3, .wav, .aac`
  - **Otros:** cualquier otro archivo
- Se ejecuta con un **doble clic** gracias al `.exe`
- No requiere abrir Python ni terminal

---

## ⚙️ Cómo usarlo

1️⃣ **Descargar o clonar el repositorio**:

```bash
git clone https://github.com/Thorqui/Organizador-Descargas.git
cd Organizador-Descargas
2️⃣ Ejecutar el script:

Opción 1: Doble clic sobre organizador_descargas.exe

Opción 2: Desde la terminal (para ver mensajes):

bash
Copiar código
.\dist\organizador_descargas.exe
3️⃣ Revisa tu carpeta de descargas y verás los archivos organizados automáticamente.

🏗️ Cómo generar el ejecutable desde Python
Si quieres construir tu propio .exe:

bash
Copiar código
pip install pyinstaller
pyinstaller --onefile organizador_descargas.py
El ejecutable aparecerá en la carpeta dist/.

🧠 Mejoras futuras
Interfaz gráfica con Tkinter (botón “Organizar Descargas”)

Configuración de carpeta de descargas personalizada

Registro de archivos movidos en un log.txt

Programación automática al iniciar sesión en Windows

👨‍💻 Autor
Aitor (Thorqui)
🔗 GitHub – Thorqui

