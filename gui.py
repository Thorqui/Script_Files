# gui.py
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from organizador import organizar_carpeta

class OrganizadorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Organizador Automático de Archivos")
        self.root.geometry("600x300")

        # Etiqueta
        self.label = tk.Label(root, text="Selecciona una carpeta para organizar:", font=("Arial", 12))
        self.label.pack(pady=10)

        # Entrada para mostrar la ruta seleccionada
        self.path_var = tk.StringVar()
        self.path_entry = tk.Entry(root, textvariable=self.path_var, width=50, state="readonly")
        self.path_entry.pack(pady=10)

        # Botón para seleccionar carpeta
        self.select_button = tk.Button(root, text="Seleccionar Carpeta", command=self.seleccionar_carpeta)
        self.select_button.pack(pady=5)

        # Opciones (dry-run y verbose)
        self.dry_run_var = tk.BooleanVar()
        self.verbose_var = tk.BooleanVar()
        self.dry_run_check = tk.Checkbutton(root, text="Modo Simulación (--dry-run)", variable=self.dry_run_var)
        self.verbose_check = tk.Checkbutton(root, text="Modo Detallado (--verbose)", variable=self.verbose_var)
        self.dry_run_check.pack(pady=5)
        self.verbose_check.pack(pady=5)

        # Botón para organizar
        self.organizar_button = tk.Button(root, text="Organizar Archivos", command=self.organizar, state="disabled")
        self.organizar_button.pack(pady=10)

        # Área de texto para mostrar resultados
        self.result_text = tk.Text(root, height=5, width=60)
        self.result_text.pack(pady=10)
        self.result_text.insert(tk.END, "Selecciona una carpeta para comenzar.\n")
        self.result_text.config(state="disabled")

    def seleccionar_carpeta(self):
        """Abre un diálogo para seleccionar una carpeta."""
        carpeta = filedialog.askdirectory()
        if carpeta:
            self.path_var.set(carpeta)
            self.organizar_button.config(state="normal")
            self.result_text.config(state="normal")
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Carpeta seleccionada: {carpeta}\n")
            self.result_text.config(state="disabled")

    def organizar(self):
        """Ejecuta la organización de la carpeta seleccionada."""
        ruta = self.path_var.get()
        dry_run = self.dry_run_var.get()
        verbose = self.verbose_var.get()

        if not ruta:
            messagebox.showerror("Error", "Por favor, selecciona una carpeta.")
            return

        self.result_text.config(state="normal")
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Organizando...\n")
        self.root.update()

        try:
            organizar_carpeta(ruta, dry_run, verbose)
            mensaje = "¡Organización completada! Revisa logs/organizador.log para detalles."
            if dry_run:
                mensaje = "Simulación completada. No se movieron archivos."
            self.result_text.insert(tk.END, mensaje + "\n")
            messagebox.showinfo("Éxito", mensaje)
        except Exception as e:
            self.result_text.insert(tk.END, f"Error: {str(e)}\n")
            messagebox.showerror("Error", f"No se pudo organizar la carpeta: {str(e)}")

        self.result_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = OrganizadorGUI(root)
    root.mainloop()