import tkinter as tk
from tkinter import messagebox
from guitarra_knowledge import Guitarra
from experta import Fact

engine = Guitarra()
engine.reset()

def obtener_recomendacion():
    nivel = nivel_var.get()
    if not nivel:
        messagebox.showwarning("Advertencia", "Por favor, seleccione su nivel.")
        return ""
    engine.declare(Fact(nivel=nivel))
    engine.run()
    recomendacion = ""
    for fact in engine.facts.values():
        if isinstance(fact, Fact) and fact.get('recomendacion'):
            recomendacion = fact['recomendacion']
    return recomendacion

def obtener_detalles():
    recomendacion = obtener_recomendacion()
    if not recomendacion:
        return
    tiempo = tiempo_var.get()
    if not tiempo:
        messagebox.showwarning("Advertencia", "Por favor, seleccione el tiempo de práctica.")
        return
    engine.declare(Fact(recomendacion=recomendacion, tiempo=tiempo))
    engine.run()
    detalle = ""
    for fact in engine.facts.values():
        if isinstance(fact, Fact) and fact.get('detalle'):
            detalle = fact['detalle']
    messagebox.showinfo("Detalles de Práctica", detalle)
    mostrar_vista_principal()  # Volver a la vista principal después de mostrar el mensaje

def etapa_nivel():
    nivel = nivel_var.get()
    if not nivel:
        messagebox.showwarning("Advertencia", "Por favor, seleccione su nivel.")
        return
    recomendacion = obtener_recomendacion()
    if not recomendacion:
        return
    messagebox.showinfo("Recomendación", recomendacion)
    for widget in root.winfo_children():
        widget.destroy()
    tk.Label(root, text="¿Cuánto tiempo al día puede dedicar?", font=("Helvetica", 16)).pack(pady=10)
    tk.Radiobutton(root, text="15 minutos", variable=tiempo_var, value='15 minutos', font=("Helvetica", 14)).pack(anchor="w", padx=20)
    tk.Radiobutton(root, text="30 minutos", variable=tiempo_var, value='30 minutos', font=("Helvetica", 14)).pack(anchor="w", padx=20)
    tk.Button(root, text="Obtener Detalles de Práctica", command=obtener_detalles, font=("Helvetica", 14)).pack(pady=20)

def mostrar_vista_principal():
    for widget in root.winfo_children():
        widget.destroy()
    tk.Label(root, text="Seleccione su nivel:", font=("Helvetica", 16)).pack(pady=10)
    tk.Radiobutton(root, text="Principiante", variable=nivel_var, value='principiante', font=("Helvetica", 14)).pack(anchor="w", padx=20)
    tk.Radiobutton(root, text="Intermedio", variable=nivel_var, value='intermedio', font=("Helvetica", 14)).pack(anchor="w", padx=20)
    tk.Radiobutton(root, text="Avanzado", variable=nivel_var, value='avanzado', font=("Helvetica", 14)).pack(anchor="w", padx=20)
    tk.Button(root, text="Obtener Recomendación", command=etapa_nivel, font=("Helvetica", 14)).pack(pady=20)

root = tk.Tk()
root.title("Sistema Experto para Aprender Guitarra")
root.geometry("400x300")  # Establece el tamaño de la ventana principal

nivel_var = tk.StringVar()
tiempo_var = tk.StringVar()

mostrar_vista_principal()

root.mainloop()
