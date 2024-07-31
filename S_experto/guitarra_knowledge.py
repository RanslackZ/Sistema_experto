# guitarra_knowledge.py
from experta import *

class Guitarra(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="find_recommendation")

    @Rule(Fact(action='find_recommendation'), Fact(nivel='principiante'))
    def acordes_basicos(self):
        self.declare(Fact(recomendacion="Aprende acordes mayores y menores"))

    @Rule(Fact(action='find_recommendation'), Fact(nivel='intermedio'))
    def tecnicas_intermedias(self):
        self.declare(Fact(recomendacion="Practica escalas pentatónicas y arpegios"))

    @Rule(Fact(action='find_recommendation'), Fact(nivel='avanzado'))
    def tecnicas_avanzadas(self):
        self.declare(Fact(recomendacion="Improvisación y solos complejos"))

    @Rule(Fact(recomendacion='Aprende acordes mayores y menores'), Fact(tiempo='15 minutos'))
    def practica_corta(self):
        self.declare(Fact(detalle="Dedica 5 minutos a practicar cada acorde (Do, Re, Mi, Fa, Sol, La, Si)"))

    @Rule(Fact(recomendacion='Aprende acordes mayores y menores'), Fact(tiempo='30 minutos'))
    def practica_media(self):
        self.declare(Fact(detalle="Dedica 15 minutos a practicar los acordes y 15 minutos a cambiar entre ellos"))

    @Rule(Fact(recomendacion='Practica escalas pentatónicas y arpegios'), Fact(tiempo='15 minutos'))
    def practica_intermedia_corta(self):
        self.declare(Fact(detalle="Dedica 5 minutos a cada escala (mayor, menor, pentatónica)"))

    @Rule(Fact(recomendacion='Practica escalas pentatónicas y arpegios'), Fact(tiempo='30 minutos'))
    def practica_intermedia_media(self):
        self.declare(Fact(detalle="Dedica 15 minutos a cada tipo de ejercicio (escalas, arpegios)"))
    
    @Rule(Fact(recomendacion='Improvisación y solos complejos'), Fact(tiempo='15 minutos'))
    def practica_avanzada_corta(self):
        self.declare(Fact(detalle="Dedica 15 minutos a estudiar una técnica avanzada"))

    @Rule(Fact(recomendacion='Improvisación y solos complejos'), Fact(tiempo='30 minutos'))
    def practica_avanzada_media(self):
        self.declare(Fact(detalle="Dedica 15 minutos a estudiar una técnica avanzada y 15 minutos a improvisar sobre una base"))
