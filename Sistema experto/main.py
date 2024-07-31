# main.py
import tkinter as tk
from interfaz import InterfazSistemaExperto

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazSistemaExperto(root)
    root.mainloop()
