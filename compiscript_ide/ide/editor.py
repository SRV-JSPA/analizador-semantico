import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class CodeEditor:
    def __init__(self, parent):
        self.text_area = ScrolledText(parent, font=("Consolas", 12), undo=True)
        self.current_file = None

    def set_content(self, text):
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, text)

    def get_content(self):
        return self.text_area.get("1.0", tk.END)
