import tkinter as tk
from tkinter import messagebox
import subprocess
import os

class Toolbar(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        tk.Button(self, text="Guardar", command=self.guardar).pack(side=tk.LEFT, padx=5)
        tk.Button(self, text="Compilar", command=self.compilar).pack(side=tk.LEFT, padx=5)

    def guardar(self):
        file = self.app.get_current_path()
        if not file:
            messagebox.showwarning("Sin archivo", "No se ha abierto ningún archivo.")
            return
        with open(file, "w", encoding="utf-8") as f:
            f.write(self.app.get_code())
        self.app.console.log(f" Archivo guardado: {file}")

    def compilar(self):
        command = ["python", "commands/antlr"]  

        try:
            result = subprocess.run(command, capture_output=True, text=True, cwd=os.getcwd())
            self.app.console.log("Compilación terminada :D")
            self.app.console.log(result.stdout)
            if result.stderr:
                self.app.console.log("!!! Errores:")
                self.app.console.log(result.stderr)
        except Exception as e:
            self.app.console.log(f"X Error al compilar: {str(e)}")
