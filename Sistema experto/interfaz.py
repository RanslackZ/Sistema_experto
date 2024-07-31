# interfaz.py
import tkinter as tk
from base_de_conocimientos import BaseDeConocimientos

class InterfazSistemaExperto:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Experto para Aprender Guitarra")
        
        self.bc = BaseDeConocimientos()

        self.tema_label = tk.Label(root, text="Seleccione un tema:")
        self.tema_label.pack()

        self.temas = ["notas_basicas", "acordes_basicos", "tipos_de_rasgueo", "tipos_de_punteo", "tecnicas_basicas"]
        self.tema_var = tk.StringVar(root)
        self.tema_var.set(self.temas[0])

        self.tema_menu = tk.OptionMenu(root, self.tema_var, *self.temas)
        self.tema_menu.pack()

        self.buscar_button = tk.Button(root, text="Buscar", command=self.mostrar_informacion)
        self.buscar_button.pack()

        self.resultado_text = tk.Text(root, height=10, width=50)
        self.resultado_text.pack()

    def mostrar_informacion(self):
        tema = self.tema_var.get()
        informacion = self.bc.obtener_informacion(tema)
        self.resultado_text.delete(1.0, tk.END)
        self.resultado_text.insert(tk.END, informacion)

