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
        self.console.log(f"[📄] Archivo abierto: {filepath}")

    def get_code(self):
        return self.editor.get_content()

    def get_current_path(self):
        return self.editor.current_file

if __name__ == "__main__":
    root = tk.Tk()
    app = IDEApp(root)
    root.mainloop()

