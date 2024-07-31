# Sistema Experto para Aprender Guitarra

Este proyecto implementa un sistema experto para recomendar prácticas de guitarra según el nivel del usuario y el tiempo disponible para la práctica diaria. El sistema usa la biblioteca experta para la lógica de inferencia y tkinter para la interfaz gráfica de usuario.
## Requisitos:

* Python 3.x
* Bibliotecas:
  * tkinter
  * experta

# Estructura del Proyecto

El proyecto está dividido en los siguientes archivos:

    main.py - Archivo principal que contiene la lógica de la interfaz gráfica.
    guitarra_knowledge.py - Archivo que contiene las reglas del sistema experto.

## Archivo "guitarra_knowledge.py"

### Este archivo define las reglas y hechos del sistema experto utilizando la biblioteca experta.


```python

    # guitarra_knowledge.py
    from experta import *
    
    class Guitarra(KnowledgeEngine):
        @Rule(Fact(nivel='principiante'))
        def acordes_basicos(self):
            self.declare(Fact(recomendacion="Aprende acordes mayores y menores"))
    
        @Rule(Fact(nivel='intermedio'))
        def tecnicas_intermedias(self):
            self.declare(Fact(recomendacion="Practica escalas pentatónicas y arpegios"))
    
        @Rule(Fact(nivel='avanzado'))
        def tecnicas_avanzadas(self):
            self.declare(Fact(recomendacion="Improvisación y solos complejos"))
    
        @Rule(Fact(recomendacion='Aprende acordes mayores y menores', tiempo='15 minutos'))
        def practica_corta(self):
            self.declare(Fact(detalle="Dedica 5 minutos a practicar cada acorde (Do, Re, Mi, Fa, Sol, La, Si)"))
    
        @Rule(Fact(recomendacion='Aprende acordes mayores y menores', tiempo='30 minutos'))
        def practica_media(self):
            self.declare(Fact(detalle="Dedica 15 minutos a practicar los acordes y 15 minutos a cambiar entre ellos"))
    
        @Rule(Fact(recomendacion='Practica escalas pentatónicas y arpegios', tiempo='15 minutos'))
        def practica_intermedia_corta(self):
            self.declare(Fact(detalle="Dedica 5 minutos a cada escala (mayor, menor, pentatónica)"))
    
        @Rule(Fact(recomendacion='Practica escalas pentatónicas y arpegios', tiempo='30 minutos'))
        def practica_intermedia_media(self):
            self.declare(Fact(detalle="Dedica 15 minutos a cada tipo de ejercicio (escalas, arpegios)"))
        
        @Rule(Fact(recomendacion='Improvisación y solos complejos', tiempo='15 minutos'))
        def practica_avanzada_corta(self):
            self.declare(Fact(detalle="Dedica 15 minutos a estudiar una técnica avanzada"))
    
        @Rule(Fact(recomendacion='Improvisación y solos complejos', tiempo='30 minutos'))
        def practica_avanzada_media(self):
            self.declare(Fact(detalle="Dedica 15 minutos a estudiar una técnica avanzada y 15 minutos a improvisar sobre una base"))

```
## Archivo "main.py"

### Este archivo contiene la lógica para la interfaz gráfica de usuario utilizando tkinter.

```python

    # main.py
    import tkinter as tk
    from tkinter import messagebox
    from guitarra_knowledge import Guitarra
    from experta import Fact
    
    engine = Guitarra()
    engine.reset()
    
    def obtener_recomendacion():
        nivel = nivel_var.get()
        engine.declare(Fact(nivel=nivel))
        engine.run()
        recomendacion = ""
        for fact in engine.facts.values():
            if isinstance(fact, Fact) and fact.get('recomendacion'):
                recomendacion = fact['recomendacion']
        return recomendacion
    
    def obtener_detalles():
        recomendacion = obtener_recomendacion()
        tiempo = tiempo_var.get()
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
        recomendacion = obtener_recomendacion()
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
```

Explicación del Código

1. Instanciación y reseteo del motor de inferencia:


```python

engine = Guitarra()
engine.reset()

```
2. Función obtener_recomendacion:
    * Declara un hecho con el nivel del usuario y ejecuta el motor de inferencia.
    * Busca en los hechos la recomendación correspondiente.

3. Función obtener_detalles:
   * Obtiene la recomendación y declara un hecho con el tiempo disponible.
   * Ejecuta el motor de inferencia y muestra los detalles de la práctica recomendada.
   * Llama a mostrar_vista_principal para volver a la vista principal.

4. Función etapa_nivel:
    * Obtiene la recomendación y muestra un mensaje con la recomendación.
    * Reconstruye la interfaz para preguntar el tiempo disponible.

5. Función mostrar_vista_principal:
    * Reconstruye la interfaz principal con las opciones de nivel.
    * Configuración de la interfaz gráfica:
        - Configura la ventana principal con un tamaño de 400x300.
        - Inicializa las variables de nivel y tiempo.
        - Llama a mostrar_vista_principal para mostrar la interfaz principal.

## Ejecución    

Para ejecutar el sistema experto, simplemente corre el archivo main.py:

```bash
    python main.py

```
> [!IMPORTANT]
> IMPORTANTE
> Asegúrate de tener todas las bibliotecas necesarias instaladas. Puedes instalarlas utilizando pip:

```bash
    pip install experta

```
