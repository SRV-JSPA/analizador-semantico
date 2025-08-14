import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import sys
from pathlib import Path

class Toolbar(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        tk.Button(self, text="Guardar",  command=self.guardar).pack(side=tk.LEFT, padx=5)
        tk.Button(self, text="Compilar", command=self.compilar).pack(side=tk.LEFT, padx=5)

    def _get_repo_root(self) -> Path:
        project_root = getattr(self.app, "project_root", None)
        if project_root:
            return Path(project_root)

        here = Path(__file__).resolve()
        repo_root = here.parents[2]  
        return repo_root

    def _get_program_dir(self) -> Path:
        return self._get_repo_root() / "program"

    def guardar(self):
        file = self.app.get_current_path()
        if not file:
            messagebox.showwarning("Sin archivo", "No se ha abierto ningún archivo.")
            return
        with open(file, "w", encoding="utf-8") as f:
            f.write(self.app.get_code())
        self.app.console.log(f"Archivo guardado: {file}")

    def compilar(self):
        program_dir = self._get_program_dir()
        if not program_dir.exists():
            messagebox.showerror("Ruta inválida", f"No se encontró la carpeta 'program':\n{program_dir}")
            return

        current_path = self.app.get_current_path()
        if current_path and current_path.endswith(".cps"):
            cps_file = Path(current_path)
        else:
            cps_file = program_dir / "archivo.cps"

        if not cps_file.exists():
            messagebox.showerror("Archivo no encontrado", f"No existe el archivo .cps:\n{cps_file}")
            return

        if current_path and Path(current_path).resolve() == cps_file.resolve():
            self.guardar()

        command = [sys.executable, "main.py", str(cps_file.resolve())]

        try:
            self.app.console.log(f"Compilando: {cps_file.name}")
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                cwd=str(program_dir) 
            )
            self.app.console.log("Compilación terminada :)")
            if result.stdout.strip():
                self.app.console.log(result.stdout)
            if result.stderr.strip():
                self.app.console.log("Error/es")
                self.app.console.log(result.stderr)
        except Exception as e:
            self.app.console.log(f"Error al compilar: {str(e)}")
