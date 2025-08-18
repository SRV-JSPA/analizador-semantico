import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess
import os
import sys
from pathlib import Path

class Toolbar(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.analyzer_path = None  

        tk.Button(self, text="Guardar", command=self.guardar).pack(side=tk.LEFT, padx=5)
        tk.Button(self, text="Compilar", command=self.compilar).pack(side=tk.LEFT, padx=5)
        tk.Button(self, text="Configurar Analizador", command=self.configurar_analizador).pack(side=tk.LEFT, padx=5)

    def configurar_analizador(self):
        """Permite al usuario seleccionar la carpeta del analizador semántico"""
        folder = filedialog.askdirectory(
            title="Selecciona la carpeta del Analizador Semántico",
            initialdir=os.getcwd()
        )
        if folder:
            main_py = Path(folder) / "main.py"
            if main_py.exists():
                self.analyzer_path = Path(folder)
                self.app.console.log(f"Analizador configurado: {folder}")
                messagebox.showinfo("Configuración exitosa", 
                                  f"Analizador semántico configurado correctamente:\n{folder}")
            else:
                messagebox.showerror("Error", 
                                   f"No se encontró main.py en:\n{folder}")

    def _find_analyzer_automatically(self) -> Path:
        """Busca automáticamente el analizador semántico en ubicaciones comunes"""
        possible_locations = [
            
            Path.cwd(),
            
            Path.cwd().parent,
            
            Path.cwd().parent / "ANALIZADOR-SEMANTICO",
            Path.cwd().parent / "analizador-semantico", 
            Path.cwd().parent / "semantic-analyzer",
            
            Path(__file__).parent.parent,
            
            Path.cwd() / "analizador",
            Path.cwd() / "semantico",
        ]
        
        for location in possible_locations:
            main_py = location / "main.py"
            analizador_py = location / "analizador_semantico.py"
            
            
            if main_py.exists() and analizador_py.exists():
                return location
        
        return None

    def _get_analyzer_dir(self) -> Path:
        """Obtiene el directorio del analizador semántico"""
        
        if self.analyzer_path and self.analyzer_path.exists():
            return self.analyzer_path
        
        
        auto_found = self._find_analyzer_automatically()
        if auto_found:
            self.analyzer_path = auto_found
            return auto_found
        
        
        here = Path(__file__).resolve()
        return here.parent.parent

    def guardar(self):
        file = self.app.get_current_path()
        if not file:
            messagebox.showwarning("Sin archivo", "No se ha abierto ningún archivo.")
            return
        try:
            with open(file, "w", encoding="utf-8") as f:
                f.write(self.app.get_code())
            self.app.console.log(f"Archivo guardado: {Path(file).name}")
        except Exception as e:
            self.app.console.log(f"Error al guardar: {str(e)}")
            messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{str(e)}")

    def compilar(self):
        
        analyzer_dir = self._get_analyzer_dir()
        main_py = analyzer_dir / "main.py"
        
        
        if not main_py.exists():
            self.app.console.log(f"No se encontró el analizador en: {analyzer_dir}")
            response = messagebox.askyesno(
                "Analizador no encontrado", 
                f"No se encontró main.py del analizador semántico en:\n{main_py}\n\n"
                "¿Deseas configurar manualmente la ubicación del analizador?"
            )
            if response:
                self.configurar_analizador()
                return
            else:
                return

        
        current_path = self.app.get_current_path()
        
        if not current_path:
            messagebox.showwarning("Sin archivo", 
                                 "No hay ningún archivo abierto. Abre un archivo .cps primero.")
            return
            
        if not current_path.endswith(".cps"):
            messagebox.showwarning("Archivo inválido", 
                                 "El archivo actual no es un archivo .cps. Selecciona un archivo .cps.")
            return

        cps_file = Path(current_path)
        
        
        if not cps_file.exists():
            messagebox.showerror("Archivo no encontrado", f"No existe el archivo .cps:\n{cps_file}")
            return

        
        self.guardar()

        
        command = [sys.executable, str(main_py), str(cps_file.resolve())]

        try:
            self.app.console.log(f"Archivo: {cps_file.name}")
            self.app.console.log(f"Analizador: {analyzer_dir}")
            
            
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                cwd=str(analyzer_dir),  
                timeout=30  
            )

            if result.stdout.strip():
                for line in result.stdout.strip().split('\n'):
                    self.app.console.log(line)
            
            if result.stderr.strip():
                for line in result.stderr.strip().split('\n'):
                    self.app.console.log(line)
            
            
                
        except Exception as e:
            self.app.console.log(f"Error al ejecutar el analizador: {str(e)}")
            messagebox.showerror("Error de ejecución", f"Error al ejecutar el analizador:\n{str(e)}")