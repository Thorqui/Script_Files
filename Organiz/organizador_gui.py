import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Mapeo de carpetas por tipo de archivo
EXTENSIONES = {
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Musica": [".mp3", ".wav", ".aac"],
}

OTROS = "Otros"

def organizar_descargas(carpeta):
    log = []
    for archivo in os.listdir(carpeta):
        ruta_completa = os.path.join(carpeta, archivo)
        if os.path.isfile(ruta_completa):
            movido = False
            for carpeta_tipo, extensiones in EXTENSIONES.items():
                if any(archivo.lower().endswith(ext) for ext in extensiones):
                    destino = os.path.join(carpeta, carpeta_tipo)
                    os.makedirs(destino, exist_ok=True)
                    shutil.move(ruta_completa, os.path.join(destino, archivo))
                    log.append(f"{archivo} → {carpeta_tipo}")
                    movido = True
                    break
            if not movido:
                destino = os.path.join(carpeta, OTROS)
                os.makedirs(destino, exist_ok=True)
                shutil.move(ruta_completa, os.path.join(destino, archivo))
                log.append(f"{archivo} → {OTROS}")
    # Guardar log
    with open(os.path.join(carpeta, "log_organizador.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(log))
    return len(log)

# --- INTERFAZ GRÁFICA ---
def seleccionar_carpeta():
    ruta = filedialog.askdirectory()
    if ruta:
        carpeta_var.set(ruta)

def ejecutar():
    carpeta = carpeta_var.get()
    if not carpeta:
        messagebox.showwarning("Atención", "Selecciona una carpeta primero")
        return
    archivos_movidos = organizar_descargas(carpeta)
    messagebox.showinfo("¡Listo!", f"Organización completada ✅\nArchivos movidos: {archivos_movidos}")

# Ventana principal
root = tk.Tk()
root.title("Organizador de Descargas")
root.geometry("400x200")

tk.Label(root, text="Selecciona la carpeta a organizar:").pack(pady=10)
carpeta_var = tk.StringVar()
tk.Entry(root, textvariable=carpeta_var, width=40).pack(pady=5)
tk.Button(root, text="Examinar", command=seleccionar_carpeta).pack(pady=5)
tk.Button(root, text="Organizar", command=ejecutar).pack(pady=10)

root.mainloop()
