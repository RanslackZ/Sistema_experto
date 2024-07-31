# base_de_conocimientos.py

class BaseDeConocimientos:
    def __init__(self):
        self.conocimientos = {
            "notas_basicas": ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"],
            "acordes_basicos": ["Do mayor", "Re mayor", "Mi mayor", "Fa mayor", "Sol mayor", "La mayor", "Si mayor"],
            "tipos_de_rasgueo": ["Rasgueo hacia abajo", "Rasgueo hacia arriba", "Rasgueo combinado"],
            "tipos_de_punteo": ["Punteo simple", "Punteo alternado"],
            "tecnicas_basicas": ["Hammer-on", "Pull-off", "Slide", "Bend"]
        }

    def obtener_informacion(self, tema):
        return self.conocimientos.get(tema, "Tema no encontrado")
