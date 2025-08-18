import tkinter as tk
from ide.file_tree import FileTree
from ide.editor import CodeEditor
from ide.console import Console
from ide.toolbar import Toolbar

class IDEApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Compiscript IDE")
        self.root.geometry("1200x700")

        self.toolbar = Toolbar(root, self)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        self.main_frame = tk.PanedWindow(root, orient=tk.HORIZONTAL)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.file_tree = FileTree(self.main_frame, self)
        self.main_frame.add(self.file_tree.frame, width=300)

        self.editor = CodeEditor(self.main_frame)
        self.main_frame.add(self.editor.text_area)

        self.console = Console(root)
        self.console.pack(fill=tk.X)

    def open_file(self, filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        self.editor.set_content(content)
        self.editor.current_file = filepath
        self.console.log(f"Archivo abierto: {filepath}")

    def get_code(self):
        return self.editor.get_content()

    def get_current_path(self):
        return self.editor.current_file

if __name__ == "__main__":
    root = tk.Tk()
    app = IDEApp(root)
    root.mainloop()

import tkinter as tk
from ide.file_tree import FileTree
from ide.editor import CodeEditor
from ide.console import Console
from ide.toolbar import Toolbar

class IDEApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Compiscript IDE - Analizador Semántico")
        self.root.geometry("1200x700")

        
        self.top_frame = tk.Frame(root)
        self.top_frame.pack(side=tk.TOP, fill=tk.X)

        self.toolbar = Toolbar(self.top_frame, self)
        self.toolbar.pack(side=tk.LEFT, fill=tk.X, expand=True)

        
        self.status_frame = tk.Frame(self.top_frame)
        self.status_frame.pack(side=tk.RIGHT, padx=10)
        
        self.status_label = tk.Label(self.status_frame, text="Sin archivo", 
                                   bg="lightgray", padx=10, pady=2)
        self.status_label.pack()

        
        self.main_frame = tk.PanedWindow(root, orient=tk.HORIZONTAL)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        
        self.file_tree = FileTree(self.main_frame, self)
        self.main_frame.add(self.file_tree.frame, width=300)

        
        self.editor = CodeEditor(self.main_frame)
        self.main_frame.add(self.editor.text_area)

        
        self.console = Console(root)
        self.console.pack(fill=tk.X)


    def open_file(self, filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            self.editor.set_content(content)
            self.editor.current_file = filepath
            
            
            filename = filepath.split('/')[-1] if '/' in filepath else filepath.split('\\')[-1]
            self.root.title(f"Compiscript IDE - {filename}")
            
            
            if filepath.endswith('.cps'):
                self.status_label.config(text=f"{filename}", bg="lightgreen")
                self.console.log(f"Archivo .cps abierto: {filename}")
            else:
                self.status_label.config(text=f"📄 {filename}", bg="lightyellow")
                self.console.log(f"Archivo abierto: {filename}")
                
        except Exception as e:
            self.console.log(f"Error al abrir archivo: {str(e)}")
            self.status_label.config(text="Error al abrir", bg="lightcoral")

    def get_code(self):
        return self.editor.get_content()

    def get_current_path(self):
        return self.editor.current_file

if __name__ == "__main__":
    root = tk.Tk()
    app = IDEApp(root)
    root.mainloop()